import os, io, requests
from docx import Document
from docx.shared import Pt, Inches
from datetime import datetime
from docx.enum.text import WD_ALIGN_PARAGRAPH
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BuiltMaterialForm, BuiltUEForm, ExcavationForm, FactForm, \
                   InclusionForm, RoomForm, SedimentaryMaterialForm, SedimentaryUEForm, \
                   PhotoForm, CustomUserCreationForm, CustomUserChangeForm, \
                   InclusionUpdateForm, FactUpdateForm, SedimentaryUEUpdateForm, BuiltUEUpdateForm
from .models import Excavation, Photo, Fact, Inclusion, Room, BuiltMaterial, \
                    SedimentaryMaterial, BuiltUE, SedimentaryUE, UE, Log
from django.conf import settings
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.mail import BadHeaderError, send_mail
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import ExcavationSerializer, PhotoSerializer,SedimentaryMaterialSerializer,\
                         BuiltMaterialSerializer, SedimentaryUESerializer, BuiltUESerializer,\
                         InclusionSerializer, RoomSerializer, FactSerializer

# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')

# ############
# EXCAVATIONS
# ############
@login_required
@permission_required('myFindings.view_excavation', raise_exception=True)
def list_allexcavations(request):
    # Get all excavations
    excavations = Excavation.objects.get_queryset().order_by('id')
    
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(excavations, 6)
        excavations = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay excavaciones para mostrar.")

    data = { 
        'entity': excavations,
        'paginator': paginator,
    }

    return render(request, 'excavations_list.html', data)

@login_required
@permission_required('myFindings.add_excavation', raise_exception=True)
def add_excavation(request):
    # Get the fields of excavation
    data = { 'form': ExcavationForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = ExcavationForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Excavaci??n creada correctamente.')
            Log.objects.create(description='El usuario %s ha creado la excavaci??n %s.' % (request.user, form.instance.n_excavacion),
                               date_and_time=datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of excavations
            return redirect(to='excavations')
        else:
            data['form'] = form

    return render(request, 'add_excavation.html', data)

@login_required
@permission_required('myFindings.change_excavation', raise_exception=True)
def modify_excavation(request, id):
    excavation = get_object_or_404(Excavation, id=id)
    
    form = ExcavationForm(instance=excavation)

    # Make the field n_excavacion readonly
    form.fields['n_excavacion'].widget.attrs['readonly'] = True

    # Save the form with the excavation data
    data = { 'form': form }

    if request.method == 'POST':
        form = ExcavationForm(data=request.POST, instance=excavation)
        if form.is_valid():       # Si es v??lido
            form.save()           # Guardarlo

            # Send a message to the user
            messages.success(request, 'Excavaci??n modificada correctamente.')
            Log.objects.create(description='El usuario %s ha modificado la excavaci??n %s.' % (request.user, excavation.n_excavacion),
                    date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            return redirect(to="excavations")

        data["form"] = form

    return render(request, 'modify_excavation.html', data)

@login_required
@permission_required('myFindings.delete_excavation', raise_exception=True)
def delete_excavation(request, id):
    # Get the excavation, if it doesn't exist, get an Http404
    excavation = get_object_or_404(Excavation, id=id)

    # Delete the excavation
    excavation.delete()    

    # Send a message to the user
    messages.success(request, 'Excavaci??n eliminada correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado la excavaci??n %s.' % (request.user, excavation.n_excavacion),
            date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="excavations")    

# ################
# SEDIMENTARY UE
# ################
@login_required
@permission_required('myFindings.view_sedimentaryue', raise_exception=True)
def list_allsedimentaryues(request):
    # Get all sedimentary ues
    sedimentaryues = SedimentaryUE.objects.get_queryset().order_by('id')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(sedimentaryues, 6)
        sedimentaryues = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay unidades sedimentarias para mostrar.")

    data = { 
        'entity': sedimentaryues,
        'paginator': paginator,
    }

    return render(request, 'sedimentaryues_list.html', data)

@login_required
@permission_required('myFindings.add_sedimentaryue', raise_exception=True)
def add_sedimentaryue(request):
    # Get the fields of the sedimentary ue
    data = { 'form': SedimentaryUEForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = SedimentaryUEForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Unidad sedimentaria creada correctamente.')
            Log.objects.create(description='El usuario %s ha creado la unidad sedimentaria UE%s.' % (request.user, form.instance.codigo),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of excavations
            return redirect(to='sedimentaryues')
        else:
            data['form'] = form

    return render(request, 'add_sedimentaryue.html', data)

@login_required
@permission_required('myFindings.change_sedimentaryue', raise_exception=True)
def modify_sedimentaryue(request, id):
    sedimentaryue = get_object_or_404(SedimentaryUE, id=id)
    
    # Save the form with the sedimentaryue data
    data = { 'form': SedimentaryUEUpdateForm(instance=sedimentaryue), 'code': sedimentaryue.codigo }

    if request.method == 'POST':
        form = SedimentaryUEUpdateForm(data=request.POST, instance=sedimentaryue, files=request.FILES)
        if form.is_valid():       # Si es v??lido
            form.save()           # Guardarlo

            # Send a message to the user
            messages.success(request, 'Unidad sedimentaria modificada correctamente.')
            Log.objects.create(description='El usuario %s ha modificado la unidad sedimentaria UE%s.' % (request.user, sedimentaryue.codigo),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            return redirect(to="sedimentaryues")

        data["form"] = form

    return render(request, 'modify_sedimentaryue.html', data)

@login_required
@permission_required('myFindings.delete_sedimentaryue', raise_exception=True)
def delete_sedimentaryue(request, id):
    # Get the sedimentary ue, if it doesn't exist, get an Http404
    sedimentaryue = get_object_or_404(SedimentaryUE, id=id)

    # Delete the sedimentaryue
    sedimentaryue.delete()    

    # Send a message to the user
    messages.success(request, 'Unidad sedimentaria eliminada correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado la unidad sedimentaria UE%s.' % (request.user, sedimentaryue.codigo),
        date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="sedimentaryues")   

# ################
# BUILT UE
# ################
@login_required
@permission_required('myFindings.view_builtue', raise_exception=True)
def list_allbuiltues(request):
    # Get all built ues
    builtues = BuiltUE.objects.get_queryset().order_by('id')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(builtues, 6)
        builtues = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay unidades construidas para mostrar.")


    data = { 
        'entity': builtues,
        'paginator': paginator,
    }

    return render(request, 'builtues_list.html', data)

@login_required
@permission_required('myFindings.add_builtue', raise_exception=True)
def add_builtue(request):
    # Get the fields of built ue
    data = { 'form': BuiltUEForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = BuiltUEForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Unidad construida creada correctamente.')
            Log.objects.create(description='El usuario %s ha creado la unidad construida UE%s.' % (request.user, form.instance.codigo),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of excavations
            return redirect(to='builtues')
        else:
            data['form'] = form

    return render(request, 'add_builtue.html', data)

@login_required
@permission_required('myFindings.change_builtue', raise_exception=True)
def modify_builtue(request, id):
    builtue = get_object_or_404(BuiltUE, id=id)
    
    # Save the form with the data of the builtue
    data = { 'form': BuiltUEUpdateForm(instance=builtue), 'code': builtue.codigo }

    if request.method == 'POST':
        form = BuiltUEUpdateForm(data=request.POST, instance=builtue, files=request.FILES)
        if form.is_valid():       # Si es v??lido
            form.save()           # Guardarlo

            # Send a message to the user
            messages.success(request, 'Unidad construida modificada correctamente.')
            Log.objects.create(description='El usuario %s ha modificado la unidad construida UE%s.' % (request.user, builtue.codigo),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            return redirect(to="builtues")

        data["form"] = form

    return render(request, 'modify_builtue.html', data)

@login_required
@permission_required('myFindings.delete_builtue', raise_exception=True)
def delete_builtue(request, id):
    # Get the sedimentary ue, if it doesn't exist, get an Http404
    builtue = get_object_or_404(BuiltUE, id=id)

    # Delete the excavation
    builtue.delete()    

    # Send a message to the user
    messages.success(request, 'Unidad construida eliminada correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado la unidad construida UE%s.' % (request.user, builtue.codigo),
        date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="builtues")


# ################
# FACT
# ################
@login_required
@permission_required('myFindings.view_fact', raise_exception=True)
def list_allfacts(request):
    # Get all facts
    facts = Fact.objects.get_queryset().order_by('id')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(facts, 6)
        facts = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay hechos para mostrar.")


    data = { 
        'entity': facts,
        'paginator': paginator,
    }

    return render(request, 'facts_list.html', data)

@login_required
@permission_required('myFindings.add_fact', raise_exception=True)
def add_fact(request):
    # Get the fields of fact
    data = { 'form': FactForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = FactForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Hecho creado correctamente.')
            Log.objects.create(description='El usuario %s ha creado el hecho %s%s.' % (request.user, form.instance.letra, form.instance.numero),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of facts
            return redirect(to='facts')
        else:
            data['form'] = form

    return render(request, 'add_fact.html', data)

@login_required
@permission_required('myFindings.change_fact', raise_exception=True)
def modify_fact(request, id):
    fact = get_object_or_404(Fact, id=id)
    
    # Save the form with the fact data
    data = { 'form': FactUpdateForm(instance=fact) }

    if request.method == 'POST':
        form = FactUpdateForm(data=request.POST, instance=fact, files=request.FILES)
        if form.is_valid():       # Si es v??lido
            form.save()           # Guardarlo

            # Send a message to the user
            messages.success(request, 'Hecho modificado correctamente.')
            Log.objects.create(description='El usuario %s ha modificado el hecho %s%s.' % (request.user, fact.letra, fact.numero),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            return redirect(to="facts")

        data["form"] = form

    return render(request, 'modify_fact.html', data)

@login_required
@permission_required('myFindings.delete_fact', raise_exception=True)
def delete_fact(request, id):
    # Get the fact, if it doesn't exist, get an Http404
    fact = get_object_or_404(Fact, id=id)

    # Delete the excavation
    fact.delete()    

    # Send a message to the user
    messages.success(request, 'Hecho eliminado correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado el hecho %s%s.' % (request.user, fact.letra, fact.numero),
        date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="facts")  

# ################
# ROOM
# ################
@login_required
@permission_required('myFindings.view_room', raise_exception=True)
def list_allrooms(request):
    # Get all rooms
    rooms = Room.objects.get_queryset().order_by('id')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(rooms, 6)
        rooms = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay estancias para mostrar.")

    data = { 
        'entity': rooms,
        'paginator': paginator,
    }

    return render(request, 'rooms_list.html', data)

@login_required
@permission_required('myFindings.add_room', raise_exception=True)
def add_room(request):
    # Get the fields of fact
    data = { 'form': RoomForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = RoomForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Estancia creada correctamente.')
            Log.objects.create(description='El usuario %s ha creado la estancia %s.' % (request.user, form.instance.n_estancia),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of facts
            return redirect(to='rooms')
        else:
            data['form'] = form

    return render(request, 'add_room.html', data) 

@login_required
@permission_required('myFindings.change_room', raise_exception=True)
def modify_room(request, id):
    room = get_object_or_404(Room, id=id)
    
    form = RoomForm(instance=room)

    # Make the field n_estancia readonly
    form.fields['n_estancia'].widget.attrs['readonly'] = True

    # Save the form with the room data
    data = { 'form': form }

    if request.method == 'POST':
        form = RoomForm(data=request.POST, instance=room, files=request.FILES)
        if form.is_valid():       # Si es v??lido
            form.save()           # Guardarlo

            # Send a message to the user
            messages.success(request, 'Estancia modificada correctamente.')
            Log.objects.create(description='El usuario %s ha modificado la estancia %s.' % (request.user, room.n_estancia),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            return redirect(to="rooms")

        data["form"] = form

    return render(request, 'modify_room.html', data)

@login_required
@permission_required('myFindings.delete_room', raise_exception=True)
def delete_room(request, id):
    # Get the room, if it doesn't exist, get an Http404
    room = get_object_or_404(Room, id=id)

    # Delete the room
    room.delete()    

    # Send a message to the user
    messages.success(request, 'Estancia eliminada correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado la estancia %s.' % (request.user, room.n_estancia),
        date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="rooms") 

# ################
# PHOTO
# ################
@login_required
@permission_required('myFindings.view_photo', raise_exception=True)
def list_allphotos(request):
    # Get all photos
    photos = Photo.objects.get_queryset().order_by('id')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(photos, 6)
        photos = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay fotos para mostrar.")

    data = { 
        'entity': photos,
        'paginator': paginator,
    }

    return render(request, 'photos_list.html', data)

@login_required
@permission_required('myFindings.add_photo', raise_exception=True)
def add_photo(request):
    # Get the fields of photo
    data = { 'form': PhotoForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = PhotoForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Foto creada correctamente.')
            Log.objects.create(description='El usuario %s ha creado la foto %s.' % (request.user, form.instance.numero),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of facts
            return redirect(to='photos')
        else:
            data['form'] = form

    return render(request, 'add_photo.html', data)

@login_required
@permission_required('myFindings.change_fotografia', raise_exception=True)
def modify_photo(request, id):
    photo = get_object_or_404(Photo, id=id)
    
    form = PhotoForm(instance=photo)

    # Make the field numero readonly
    form.fields['numero'].widget.attrs['readonly'] = True

    # Save the form with the photo data
    data = { 'form': form }

    if request.method == 'POST':
        form = PhotoForm(data=request.POST, instance=photo, files=request.FILES)
        if form.is_valid():       # Si es v??lido
            form.save()           # Guardarlo

            # Send a message to the user
            messages.success(request, 'Foto modificada correctamente.')
            Log.objects.create(description='El usuario %s ha modificado la foto %s.' % (request.user, photo.numero),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            return redirect(to="photos")

        data["form"] = form

    return render(request, 'modify_photo.html', data)
 
@login_required
@permission_required('myFindings.delete_photo', raise_exception=True)
def delete_photo(request, id):
    # Get the photo, if it doesn't exist, get an Http404
    photo = get_object_or_404(Photo, id=id)

    # Delete the photo
    photo.delete()    

    # Send a message to the user
    messages.success(request, 'Foto eliminada correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado la foto %s.' % (request.user, photo.numero),
        date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="photos") 

# ################
# INCLUSION
# ################
@login_required
@permission_required('myFindings.view_inclusion', raise_exception=True)
def list_allinclusions(request):
    # Get all photos
    inclusions = Inclusion.objects.get_queryset().order_by('id')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(inclusions, 6)
        inclusions = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay inclusiones para mostrar.")

    data = { 
        'entity': inclusions,
        'paginator': paginator,
    }

    return render(request, 'inclusions_list.html', data)

@login_required
@permission_required('myFindings.add_inclusion', raise_exception=True)
def add_inclusion(request):
    # Get the fields of inclusion
    data = { 'form': InclusionForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = InclusionForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Inclusion creada correctamente.')
            Log.objects.create(description='El usuario %s ha creado la inclusi??n %s para UE%s.' % (request.user, form.instance.tipo, form.instance.uesedimentaria.codigo),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of facts
            return redirect(to='inclusions')
        else:
            data['form'] = form

    return render(request, 'add_inclusion.html', data)

@login_required
@permission_required('myFindings.change_inclusion', raise_exception=True)
def modify_inclusion(request, id):
    inclusion = get_object_or_404(Inclusion, id=id)
    
    # Save the form with the inclusion data
    data = { 'form': InclusionUpdateForm(instance=inclusion) }

    if request.method == 'POST':
        form = InclusionUpdateForm(data=request.POST, instance=inclusion, files=request.FILES)
        if form.is_valid():       # Si es v??lido
            form.save()           # Guardarlo

            # Send a message to the user
            messages.success(request, 'Inclusion modificada correctamente.')
            Log.objects.create(description='El usuario %s ha modificado la inclusi??n %s para UE%s.' % (request.user, inclusion.tipo, inclusion.uesedimentaria.codigo),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            return redirect(to="inclusions")

        data["form"] = form

    return render(request, 'modify_inclusion.html', data)

@login_required
@permission_required('myFindings.delete_inclusion', raise_exception=True)
def delete_inclusion(request, id):
    # Get the inclusion, if it doesn't exist, get an Http404
    inclusion = get_object_or_404(Inclusion, id=id)

    # Delete the inclusion
    inclusion.delete()    

    # Send a message to the user
    messages.success(request, 'Inclusion eliminada correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado la inclusi??n %s para UE%s.' % (request.user, inclusion.tipo, inclusion.uesedimentaria.codigo),
        date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="inclusions")

# #####################
# SEDIMENTARY MATERIAL
# #####################
@login_required
@permission_required('myFindings.view_sedimentarymaterial', raise_exception=True)
def list_allsedimentarymaterials(request):
    # Get all sedimentary materials
    sedimentarymaterials = SedimentaryMaterial.objects.get_queryset().order_by('nombre')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(sedimentarymaterials, 6)
        sedimentarymaterials = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay materiales sedimentarios para mostrar.")

    data = { 
        'entity': sedimentarymaterials,
        'paginator': paginator,
    }

    return render(request, 'sedimentarymaterials_list.html', data)

@login_required
@permission_required('myFindings.add_sedimentarymaterial', raise_exception=True)
def add_sedimentarymaterial(request):
    # Get the fields of sedimentary materials
    data = { 'form': SedimentaryMaterialForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = SedimentaryMaterialForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Material sedimentario creado correctamente.')
            Log.objects.create(description='El usuario %s ha creado el material sedimentario %s.' % (request.user, form.instance.nombre),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of facts
            return redirect(to='sedimentarymaterials')
        else:
            data['form'] = form

    return render(request, 'add_sedimentarymaterial.html', data)

@login_required
@permission_required('myFindings.delete_sedimentarymaterial', raise_exception=True)
def delete_sedimentarymaterial(request, nombre):
    # Get the sedimentary material, if it doesn't exist, get an Http404
    sedimentarymaterial = get_object_or_404(SedimentaryMaterial, nombre=nombre)

    # Delete the sedimentary material
    sedimentarymaterial.delete()    

    # Send a message to the user
    messages.success(request, 'Material sedimentario eliminado correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado el material sedimentario %s.' % (request.user, nombre),
        date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="sedimentarymaterials")

# #####################
# BUILT MATERIAL
# #####################
@login_required
@permission_required('myFindings.view_builtmaterial', raise_exception=True)
def list_allbuiltmaterials(request):
    # Get all built materials
    builtmaterials = BuiltMaterial.objects.get_queryset().order_by('nombre')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(builtmaterials, 6)
        builtmaterials = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay materiales construidos para mostrar.")

    data = { 
        'entity': builtmaterials,
        'paginator': paginator,
    }

    return render(request, 'builtmaterials_list.html', data)

@login_required
@permission_required('myFindings.add_builtmaterial', raise_exception=True)
def add_builtmaterial(request):
    # Get the fields of sedimentary materials
    data = { 'form': BuiltMaterialForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = BuiltMaterialForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Send a message to the user
            messages.success(request, 'Material construido creado correctamente.')
            Log.objects.create(description='El usuario %s ha creado el material construido %s.' % (request.user, form.instance.nombre),
                date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Redirect to the list of facts
            return redirect(to='builtmaterials')
        else:
            data['form'] = form

    return render(request, 'add_builtmaterial.html', data)

@login_required
@permission_required('myFindings.delete_builtmaterial', raise_exception=True)
def delete_builtmaterial(request, nombre):
    # Get the built material, if it doesn't exist, get an Http404
    builtmaterial = get_object_or_404(BuiltMaterial, nombre=nombre)

    # Delete the built material
    builtmaterial.delete()    

    # Send a message to the user
    messages.success(request, 'Material construido eliminado correctamente.')
    Log.objects.create(description='El usuario %s ha eliminado el material construido %s.' % (request.user, nombre),
        date_and_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return redirect(to="builtmaterials")

# ####################
# SPECIFIC LISTINGS  
# ####################
@login_required
@permission_required('myFindings.view_excavation', raise_exception=True)
@permission_required('myFindings.view_sedimentaryue', raise_exception=True)
@permission_required('myFindings.view_builtue', raise_exception=True)
def list_excavationues(request, id):
    # Get the excavation
    excavation = get_object_or_404(Excavation, id=id)

    # Find all associated sedimentary stratigraphic units
    sedimentaryues = SedimentaryUE.objects.get_queryset().filter(excavacion__id=id).order_by('id')

    page1 = request.GET.get('page1', 1)
    try:
        paginator1 = Paginator(sedimentaryues, 6)
        sedimentaryues = paginator1.page(page1)
    except EmptyPage:
        raise Http404("No hay unidades sedimentarias para mostrar.")

    # Find all associated built stratigraphic units
    builtues = BuiltUE.objects.get_queryset().filter(excavacion__id=id).order_by('id')

    page2 = request.GET.get('page2', 1)
    try:
        paginator2 = Paginator(builtues, 6)
        builtues = paginator2.page(page2)
    except EmptyPage:
        raise Http404("No hay unidades construidas para mostrar.")

    data = { 
        'sedimentaryues': sedimentaryues, 
        'builtues': builtues, 
        'n_excavacion': excavation.n_excavacion,
        'paginator1': paginator1,
        'paginator2': paginator2,
    }

    return render(request, 'excavationues.html', data)

@login_required
@permission_required('myFindings.view_room', raise_exception=True)
@permission_required('myFindings.view_fact', raise_exception=True)
def list_roomfacts(request, id):
    # Get the room
    room = get_object_or_404(Room, id=id)

    # Find all associated facts
    facts = Fact.objects.get_queryset().filter(estancia__id=id).order_by('id')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(facts, 6)
        facts = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay hechos para mostrar.")

    data = { 'entity': facts,  'n_room': room.n_estancia}

    return render(request, 'facts_list.html', data)

@login_required
@permission_required('myFindings.view_fact', raise_exception=True)
@permission_required('myFindings.view_sedimentaryue', raise_exception=True)
@permission_required('myFindings.view_builtue', raise_exception=True)
def list_factues(request, id):
    # Get the fact
    fact = get_object_or_404(Fact, id=id)

    # Find all associated sedimentary stratigraphic units
    sedimentaryues = SedimentaryUE.objects.get_queryset().filter(hecho__id=id).order_by('id')

    page1 = request.GET.get('page1', 1)
    try:
        paginator1 = Paginator(sedimentaryues, 6)
        sedimentaryues = paginator1.page(page1)
    except EmptyPage:
        raise Http404("No hay unidades sedimentarias para mostrar.")
    
    # Find all associated built stratigraphic units
    builtues = BuiltUE.objects.get_queryset().filter(hecho__id=id).order_by('id')

    page2 = request.GET.get('page2', 1)
    try:
        paginator2 = Paginator(builtues, 6)
        builtues = paginator2.page(page2)
    except EmptyPage:
        raise Http404("No hay unidades construidas para mostrar.")

    nombre = fact.letra + fact.numero
    data = { 
        'sedimentaryues': sedimentaryues,
        'builtues': builtues,
        'n_hecho': nombre,
        'paginator1': paginator1,
        'paginator2': paginator2,
    }

    return render(request, 'excavationues.html', data)

# ######################
# Django authentication
# ######################
def register(request):
    # Get the fields of the registration form
    data = { 'form': CustomUserCreationForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = CustomUserCreationForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            user = form.save()         # Save form
            # default to non-active
            user.is_active = False
            user.save()

            # Send an email to the archeologist administering the site
            template_data = {
                'user': user,
                'protocol': 'http',
                'domain': request.get_host(),
            }
            send_email(subject='Verificaci??n de registro', from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[settings.EMAIL_HOST_USER], html_message='registration/registration_check.html', data=template_data)

            return render(request, 'registration/register_confirm.html')

        else:
            data['form'] = form

    return render(request, 'registration/register.html', data)

def send_email(subject, from_email, recipient_list, message='',
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None, data=None):
              
    if (html_message is not None):
        template = get_template(html_message)

        if data is not None:
            html_message = template.render(data)
    
    # Send the email
    try:
        send_mail(subject, message, from_email, recipient_list,
                fail_silently=fail_silently, auth_user=auth_user,
                auth_password=auth_password, connection=connection,
                html_message=html_message)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

def send_email_password_reset(request):
    try:
        # Get the user
        user = User.objects.get(email=request.POST['email']) 
    except User.DoesNotExist:
        return redirect(to='password_reset_done')
    
    # Get the fields of the reset form
    data = { 'user': user,
             'protocol': 'http', 
             'domain': request.get_host(),
             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
             'token': default_token_generator.make_token(user),
    }
    
    if request.method == 'POST':
        # Get the data entered by the user
        form = PasswordResetForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            send_email(subject='MyFindings: restablecer contrase??a', from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user.email], html_message='registration/password_reset_email.html', data=data)

            return redirect(to='password_reset_done')
        else:
            data['form'] = form

    return redirect(to='password_reset', context=data)

# #####################
# AUXILIARY DECORATOR 
# ####################
def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        # Raise a permission denied error instead of returning False
        raise PermissionDenied

    return user_passes_test(in_groups)

@login_required
@group_required('Staff')
def staff_panel(request):
    # Get all excavations
    users = User.objects.filter(is_superuser=False)
    staff_users = User.objects.filter(groups__name__in=['Staff'])
  
    # Exclude the users that are already staff
    users = users.exclude(id__in=staff_users.values_list('id', flat=True))
            
    data = { 'users': users}
    return render(request, 'staff_panel.html', data)

@login_required
@group_required('Staff')
def change_perms(request, id):
    # Get the user
    user = get_object_or_404(User, id=id)

    # Save the inicial value of is_active field
    was_active = user.is_active

    # Fill the form with the user's data
    data = { 'form': CustomUserChangeForm(instance=user) }

    # Get the fields for the emails
    template_data = {
        'user': user,
        'protocol': 'http',
        'domain': request.get_host(),
    }

    if request.method == 'POST':
        # Get the data entered by the user
        form = CustomUserChangeForm(data=request.POST, instance=user)
        
        if(form.is_valid()):        # Check if valid
            if was_active and not form.cleaned_data['is_active']:
                # If the user is active and is deactivated, send an email to the user              
                send_email(subject='MyFindings: cuenta desactivada', from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user.email], html_message='registration/account_deactivated.html', data=template_data)
            
            form.save()      # Save form

            # Check if the is_active field was changed
            if(not was_active and form.cleaned_data['is_active']):

                # Send an email to the user
                send_email(subject='MyFindings: cuenta activada', from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user.email], html_message='registration/account_activated.html', data=template_data)
     
            return redirect(to='staff_panel')
        
        data['form'] = form

    return render(request, 'change_perms.html', data)


# ######################
# REPORT GENERATOR
# ######################
def excavation_summary(excavation):
    description = 'Excavaci??n '
    
    if excavation.nombre:
        description += 'con nombre ' + excavation.nombre

    if excavation.n_excavacion:
        description += ', identificada por el n??mero de excavaci??n ' + excavation.n_excavacion 

    if excavation.latitud and excavation.longitud:
        description += ', que se encuentra localizada en los puntos de coordenadas latitud ' \
        + str(excavation.latitud) + ' y longitud ' + str(excavation.longitud)

    if excavation.altura:
        description += ', a una altura de ' + str(excavation.altura) + ' metros'

    description += '.'

    return description

def get_relations_generic(all):
    ues = ''

    for ue in all:
        ues += 'UE' + ue.codigo
        # Add a coma except last item
        if ue != all.last():
            ues += ', '

    ues += '; '
    return ues

def get_relations_ue(ue):
    relations = ''

    # Check if the ManyToMany field is not empty
    if ue.igual_a.all():
        relations += 'es igual a: '
        # Go through the list of relations
        relations += get_relations_generic(ue.igual_a.all())

    if ue.equivalente_a.all():
        relations += 'es equivalente a: '
        # Go through the list of relations
        relations += get_relations_generic(ue.equivalente_a.all())

    if ue.sobre.all():
        relations += 'est?? sobre: '
        # Go through the list of relations
        relations += get_relations_generic(ue.sobre.all())

    if ue.bajo.all():
        relations += 'est?? bajo: '
        # Go through the list of relations
        relations += get_relations_generic(ue.bajo.all())

    relations += '.'

    return relations

def ue_summary(ue):
    description = ''

    if ue.sector and ue.hecho:
        description += 'ubicada en el sector ' + str(ue.sector) + ' '
        description += 'formando parte del hecho ' + str(ue.hecho) + ';'

    description += 'Relaciones estratigr??ficas: '
    description += get_relations_ue(ue)
    
    if ue.cota_superior:
        description += 'Cota superior: ' + str(ue.cota_superior) + '. '

    if ue.cota_inferior:
        description += 'Cota inferior: ' + str(ue.cota_inferior) + '. '

    if ue.pendiente_superior:
        description += 'Pendiente superior: ' + str(ue.pendiente_superior) + '. '

    if ue.pendiente_inferior:
        description += 'Pendiente inferior: ' + str(ue.pendiente_inferior) + '. '

    if ue.periodo or ue.fase or ue.tpq or ue.taq:
        description += 'Cronolog??a: '
    if ue.periodo:
        description += ue.periodo + '. '
    if ue.fase: 
        description += 'Fase: ' + ue.fase + '. '
    if ue.tpq and ue.taq:
        description += 'TPQ: ' + str(ue.tpq) + ' / ' + 'TAQ: ' + str(ue.taq) + '.'

    return description

def fact_summary(fact):
    description = ''

    if fact.estancia:
        description += 'perteneciente a la estancia ' + str(fact.estancia) + '; '

    if fact.definicion:
        description += 'Definici??n: ' + fact.definicion + '; '

    if fact.comentarios:
        description += 'Comentarios: ' + fact.comentarios + '; '

    if fact.sector and fact.zona:
        description += 'ubicado en el sector ' + str(fact.sector) + ' en la zona ' + str(fact.zona) + '; '

    if fact.fase or fact.tpq or fact.taq:
        description += 'Cronolog??a: '

    if fact.fase: 
        description += 'Fase: ' + fact.fase + '. '
    if fact.tpq and fact.taq:
        description += 'TPQ: ' + str(fact.tpq) + ' / ' + 'TAQ: ' + str(fact.taq) + '.'

    return description

def get_related_facts(excavation):
    related_facts = []

    # Get the list of related ues
    ues = UE.objects.filter(excavacion=excavation)
    if ues:
        # Create a list of unique values
        for ue in ues:
            if ue.hecho:
                related_facts.append(ue.hecho)

        # Get only unic values
        related_facts = list(set(related_facts))

    return related_facts

def generate_report(request, id):
    excavation = get_object_or_404(Excavation, id=id)   # Get the excavation   

    document = Document()

    # Change the font size
    document.styles['Normal'].font.size = Pt(12)

    # Add a title
    h = document.add_heading('Informe de la excavaci??n ' + str(excavation.n_excavacion), 0)
    if excavation.nombre:
        h.add_run(': ' + excavation.nombre)
    
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # EXCAVATION
    # ---------------
    document.add_heading('Resumen general', level=1)
    document.add_paragraph(excavation_summary(excavation))
    # ---------------

    # FACTS
    # ---------------
    document.add_heading('Hechos', level=2)
    facts = get_related_facts(excavation)
    if facts:
        for fact in facts:
            # Add a new paragraph
            p = document.add_paragraph()
            p.add_run(fact.letra + fact.numero + ': ').bold = True
            p.add_run(fact_summary(fact))
            
            if fact.croquis_plan:
                p = document.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run('Croquis del plan').italic  = True
                response = requests.get(fact.croquis_plan.url)
                binary_img = io.BytesIO(response.content)
                document.add_picture(binary_img, width=Inches(2))
                picture_paragraph = document.paragraphs[-1]
                picture_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

            if fact.croquis_seccion:
                p = document.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run('Croquis de la secci??n').italic = True
                response = requests.get(fact.croquis_seccion.url)
                binary_img = io.BytesIO(response.content)
                document.add_picture(binary_img, width=Inches(2))
                picture_paragraph = document.paragraphs[-1]
                picture_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        document.add_paragraph('No se han encontrado hechos relacionados con la excavaci??n.')
    # ---------------

    # STRATIGRAPHIC UNITS
    # --------------------
    document.add_heading('Unidades estratigr??ficas', level=2)
    p = document.add_paragraph()
    p.add_run('Unidades sedimentarias').bold = True

    # Get stratigraphics units that has excavacion like foreign key
    sedimentaryues = SedimentaryUE.objects.filter(excavacion=excavation)
    if sedimentaryues:
        # Go through all the sedimentary units
        for sedimentaryue in sedimentaryues:
            # Add a new paragraph
            p = document.add_paragraph()
            p.add_run('UE' + sedimentaryue.codigo + ': ').bold = True
            p.add_run(' unidad sedimentaria; ')
            p.add_run(ue_summary(sedimentaryue))
    else:
        document.add_paragraph('No hay unidades sedimentarias registradas.')

    p2 = document.add_paragraph()
    p2.add_run('Unidades construidas').bold = True

    # Get stratigraphics units that has excavacion like foreign key
    builtues = BuiltUE.objects.filter(excavacion=excavation)
    # Checks if there are any built units
    if builtues:
        # Go through all the built units
        for builtue in builtues:
            # Add a new paragraph
            p = document.add_paragraph()
            p.add_run('UE' + builtue.codigo + ': ').bold = True
            p.add_run(' unidad construida; ')
            p.add_run(ue_summary(builtue))
    else:
        document.add_paragraph('No hay unidades construidas registradas.')
    # --------------------

    document.add_page_break()

    # Save document to memory and download to the user's browser 
    document_data = io.BytesIO()
    document.save(document_data)
    document_data.seek(0)
    response = HttpResponse(document_data.getvalue())
    filename = 'Informe de la excavaci??n ' + str(excavation.n_excavacion) + '.docx'
    response["Content-Disposition"] = 'attachment; filename = "' + filename + '"'
    response["Content-Encoding"] = "UTF-8"
    
    return response

# ######################
# API REST
# ######################
class ExcavationViewSet(viewsets.ModelViewSet):
    queryset = Excavation.objects.all()
    serializer_class = ExcavationSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class InclusionViewSet(viewsets.ModelViewSet):
    queryset = Inclusion.objects.all()
    serializer_class = InclusionSerializer

class SedimentaryUEViewSet(viewsets.ModelViewSet):
    queryset = SedimentaryUE.objects.all()
    lookup_field = 'codigo'
    serializer_class = SedimentaryUESerializer

class BuiltUEViewSet(viewsets.ModelViewSet):
    queryset = BuiltUE.objects.all()
    lookup_field = 'codigo'
    serializer_class = BuiltUESerializer

class SedimentaryMaterialViewSet(viewsets.ModelViewSet):
    queryset = SedimentaryMaterial.objects.all()
    serializer_class = SedimentaryMaterialSerializer

class BuiltMaterialViewSet(viewsets.ModelViewSet):
    queryset = BuiltMaterial.objects.all()
    serializer_class = BuiltMaterialSerializer
    lookup_field = 'codigo'

class FactViewSet(viewsets.ModelViewSet):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'groups': [group.name for group in user.groups.all()],
            'user_permissions': [permission for permission in user.get_all_permissions()]
        })

# ######################
# LOG SYSTEM
# ######################
@login_required
@group_required('Staff')
def process_logs(request):

    logs = Log.objects.get_queryset().order_by('-date_and_time')

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(logs, 7)
        logs = paginator.page(page)
    except EmptyPage:
        raise Http404("No hay m??s logs para mostrar.")

    data = { 
        'entity': logs,
        'paginator': paginator,
    }

    return render(request, 'logs.html', data)

@login_required
@group_required('Staff')
def download_logs(request):
    logs = []
    logssaved = Log.objects.get_queryset().order_by('-date_and_time')

    for log in logssaved:
        logs.append('[ ' + str(log.date_and_time) + ' ] => ' + log.description) 

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="myFindings.txt"'
    response.write('\n'.join(logs))

    return response
