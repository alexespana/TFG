from django.shortcuts import render, redirect, get_object_or_404
from .forms import BuiltMaterialForm, BuiltUEForm, ExcavationForm, FactForm, InclusionForm, RoomForm, SedimentaryMaterialForm, SedimentaryUEForm, PhotoForm
from .models import UE, Excavacion, Fotografia, Hecho, Inclusion, Estancia, MaterialConstruida, MaterialSedimentaria, UEConstruida, UESedimentaria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

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
def list_allexcavations(request):
    # Get all excavations
    excavations = Excavacion.objects.all()
    data = { 'excavations': excavations}

    return render(request, 'excavations_list.html', data)


def add_excavation(request):
    # Get the fields of excavation
    data = { 'form': ExcavationForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = ExcavationForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of excavations
            return redirect(to='excavations')
        else:
            data['form'] = form

    return render(request, 'add_excavation.html', data)

def modify_excavation(request, id):
    excavation = get_object_or_404(Excavacion, id=id)
    
    # Guardar el formulario con los datos del cuadro
    data = { 'form': ExcavationForm(instance=excavation) }

    if request.method == 'POST':
        form = ExcavationForm(data=request.POST, instance=excavation)
        if form.is_valid():       # Si es válido
            form.save()           # Guardarlo

            return redirect(to="excavations")

        data["form"] = form

    return render(request, 'modify_excavation.html', data)

def delete_excavation(request, id):
    # Get the excavation, if it doesn't exist, get an Http404
    excavation = get_object_or_404(Excavacion, id=id)

    # Delete the excavation
    excavation.delete()    

    return redirect(to="excavations")    

# ################
# SEDIMENTARY UE
# ################
def list_allsedimentaryues(request):
    # Get all sedimentary ues
    sedimentaryues = UESedimentaria.objects.all()
    data = { 'sedimentaryues': sedimentaryues}

    return render(request, 'sedimentaryues_list.html', data)

def add_sedimentaryue(request):
    # Get the fields of the sedimentary ue
    data = { 'form': SedimentaryUEForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = SedimentaryUEForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of excavations
            return redirect(to='sedimentaryues')
        else:
            data['form'] = form

    return render(request, 'add_sedimentaryue.html', data)

def modify_sedimentaryue(request, id):
    sedimentaryue = get_object_or_404(UESedimentaria, id=id)
    
    # Guardar el formulario con los datos del cuadro
    data = { 'form': SedimentaryUEForm(instance=sedimentaryue) }

    if request.method == 'POST':
        form = SedimentaryUEForm(data=request.POST, instance=sedimentaryue, files=request.FILES)
        if form.is_valid():       # Si es válido
            form.save()           # Guardarlo

            return redirect(to="sedimentaryues")

        data["form"] = form

    return render(request, 'modify_sedimentaryue.html', data)

def delete_sedimentaryue(request, id):
    # Get the sedimentary ue, if it doesn't exist, get an Http404
    sedimentaryue = get_object_or_404(UESedimentaria, id=id)

    # Delete the sedimentaryue
    sedimentaryue.delete()    

    return redirect(to="sedimentaryues")   

# ################
# BUILT UE
# ################
def list_allbuiltues(request):
    # Get all built ues
    builtues = UEConstruida.objects.all()
    data = { 'builtues': builtues}

    return render(request, 'builtues_list.html', data)

def add_builtue(request):
    # Get the fields of built ue
    data = { 'form': BuiltUEForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = BuiltUEForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of excavations
            return redirect(to='builtues')
        else:
            data['form'] = form

    return render(request, 'add_builtue.html', data)

def modify_builtue(request, id):
    builtue = get_object_or_404(UEConstruida, id=id)
    
    # Guardar el formulario con los datos del cuadro
    data = { 'form': BuiltUEForm(instance=builtue) }

    if request.method == 'POST':
        form = BuiltUEForm(data=request.POST, instance=builtue, files=request.FILES)
        if form.is_valid():       # Si es válido
            form.save()           # Guardarlo

            return redirect(to="builtues")

        data["form"] = form

    return render(request, 'modify_builtue.html', data)

def delete_builtue(request, id):
    # Get the sedimentary ue, if it doesn't exist, get an Http404
    builtue = get_object_or_404(UEConstruida, id=id)

    # Delete the excavation
    builtue.delete()    

    return redirect(to="builtues")


# ################
# FACT
# ################
def list_allfacts(request):
    # Get all facts
    facts = Hecho.objects.all()
    data = { 'facts': facts}

    return render(request, 'facts_list.html', data)

def add_fact(request):
    # Get the fields of fact
    data = { 'form': FactForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = FactForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of facts
            return redirect(to='facts')
        else:
            data['form'] = form

    return render(request, 'add_fact.html', data)

def modify_fact(request, id):
    fact = get_object_or_404(Hecho, id=id)
    
    # Guardar el formulario con los datos del cuadro
    data = { 'form': FactForm(instance=fact) }

    if request.method == 'POST':
        form = FactForm(data=request.POST, instance=fact, files=request.FILES)
        if form.is_valid():       # Si es válido
            form.save()           # Guardarlo

            return redirect(to="facts")

        data["form"] = form

    return render(request, 'modify_fact.html', data)

def delete_fact(request, id):
    # Get the fact, if it doesn't exist, get an Http404
    fact = get_object_or_404(Hecho, id=id)

    # Delete the excavation
    fact.delete()    

    return redirect(to="facts")  

# ################
# ROOM
# ################
def list_allrooms(request):
    # Get all rooms
    rooms = Estancia.objects.all()
    data = { 'rooms': rooms}

    return render(request, 'rooms_list.html', data)

def add_room(request):
    # Get the fields of fact
    data = { 'form': RoomForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = RoomForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of facts
            return redirect(to='rooms')
        else:
            data['form'] = form

    return render(request, 'add_room.html', data) 

def modify_room(request, id):
    room = get_object_or_404(Estancia, id=id)
    
    # Guardar el formulario con los datos del cuadro
    data = { 'form': RoomForm(instance=room) }

    if request.method == 'POST':
        form = RoomForm(data=request.POST, instance=room, files=request.FILES)
        if form.is_valid():       # Si es válido
            form.save()           # Guardarlo

            return redirect(to="rooms")

        data["form"] = form

    return render(request, 'modify_room.html', data)

def delete_room(request, id):
    # Get the room, if it doesn't exist, get an Http404
    room = get_object_or_404(Estancia, id=id)

    # Delete the room
    room.delete()    

    return redirect(to="rooms") 

# ################
# PHOTO
# ################
def list_allphotos(request):
    # Get all photos
    photos = Fotografia.objects.all()
    data = { 'photos': photos}

    return render(request, 'photos_list.html', data)

def add_photo(request):
    # Get the fields of photo
    data = { 'form': PhotoForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = PhotoForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of facts
            return redirect(to='photos')
        else:
            data['form'] = form

    return render(request, 'add_photo.html', data)

def modify_photo(request, id):
    photo = get_object_or_404(Fotografia, id=id)
    
    # Guardar el formulario con los datos del cuadro
    data = { 'form': PhotoForm(instance=photo) }

    if request.method == 'POST':
        form = PhotoForm(data=request.POST, instance=photo, files=request.FILES)
        if form.is_valid():       # Si es válido
            form.save()           # Guardarlo

            return redirect(to="photos")

        data["form"] = form

    return render(request, 'modify_photo.html', data)
 
def delete_photo(request, id):
    # Get the photo, if it doesn't exist, get an Http404
    photo = get_object_or_404(Fotografia, id=id)

    # Delete the photo
    photo.delete()    

    return redirect(to="photos") 

# ################
# INCLUSION
# ################
def list_allinclusions(request):
    # Get all photos
    inclusions = Inclusion.objects.all()
    data = { 'inclusions': inclusions}

    return render(request, 'inclusions_list.html', data)

def add_inclusion(request):
    # Get the fields of inclusion
    data = { 'form': InclusionForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = InclusionForm(data=request.POST, files=request.FILES)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of facts
            return redirect(to='inclusions')
        else:
            data['form'] = form

    return render(request, 'add_inclusion.html', data)


def modify_inclusion(request, id):
    inclusion = get_object_or_404(Inclusion, id=id)
    
    # Guardar el formulario con los datos del cuadro
    data = { 'form': InclusionForm(instance=inclusion) }

    if request.method == 'POST':
        form = InclusionForm(data=request.POST, instance=inclusion, files=request.FILES)
        if form.is_valid():       # Si es válido
            form.save()           # Guardarlo

            return redirect(to="inclusions")

        data["form"] = form

    return render(request, 'modify_inclusion.html', data)

def delete_inclusion(request, id):
    # Get the inclusion, if it doesn't exist, get an Http404
    inclusion = get_object_or_404(Inclusion, id=id)

    # Delete the inclusion
    inclusion.delete()    

    return redirect(to="inclusions")

# #####################
# SEDIMENTARY MATERIAL
# #####################
def list_allsedimentarymaterials(request):
    # Get all sedimentary materials
    sedimentarymaterials = MaterialSedimentaria.objects.all()
    data = { 'sedimentarymaterials': sedimentarymaterials}

    return render(request, 'sedimentarymaterials_list.html', data)

def add_sedimentarymaterial(request):
    # Get the fields of sedimentary materials
    data = { 'form': SedimentaryMaterialForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = SedimentaryMaterialForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of facts
            return redirect(to='allsedimentarymaterials_list')
        else:
            data['form'] = form

    return render(request, 'add_sedimentarymaterial.html', data)

def modify_sedimentarymaterial(request):
    pass

def delete_sedimentarymaterial(request, nombre):
    # Get the sedimentary material, if it doesn't exist, get an Http404
    sedimentarymaterial = get_object_or_404(MaterialSedimentaria, nombre=nombre)

    # Delete the sedimentary material
    sedimentarymaterial.delete()    

    return redirect(to="allsedimentarymaterials_list")

# #####################
# BUILT MATERIAL
# #####################
def list_allbuiltmaterials(request):
    # Get all built materials
    builtmaterials = MaterialConstruida.objects.all()
    data = { 'builtmaterials': builtmaterials}

    return render(request, 'builtmaterials_list.html', data)

def add_builtmaterial(request):
    # Get the fields of sedimentary materials
    data = { 'form': BuiltMaterialForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = BuiltMaterialForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of facts
            return redirect(to='allbuiltmaterials_list')
        else:
            data['form'] = form

    return render(request, 'add_builtmaterial.html', data)

def modify_builtmaterial(request):
    pass

def delete_builtmaterial(request, nombre):
    # Get the built material, if it doesn't exist, get an Http404
    builtmaterial = get_object_or_404(MaterialConstruida, nombre=nombre)

    # Delete the built material
    builtmaterial.delete()    

    return redirect(to="allbuiltmaterials_list")

# ####################
# SPECIFIC LISTINGS  
# ####################
def list_excavationues(request, id):
    # Get the excavation
    excavation = get_object_or_404(Excavacion, id=id)

    # Find all associated sedimentary stratigraphic units
    sedimentaryues = UESedimentaria.objects.filter(excavacion__id=id)

    # Find all associated built stratigraphic units
    builtues = UEConstruida.objects.filter(excavacion__id=id)

    data = { 'sedimentaryues': sedimentaryues, 'builtues': builtues, 'n_excavacion': excavation.n_excavacion}

    return render(request, 'excavationues.html', data)

def list_roomfacts(request, id):
    # Get the room
    room = get_object_or_404(Estancia, id=id)

    # Find all associated facts
    facts = Hecho.objects.filter(estancia__id=id)

    data = { 'facts': facts,  'n_room': room.n_estancia}

    return render(request, 'facts_list.html', data)

def list_factues(request, id):
    # Get the fact
    fact = get_object_or_404(Hecho, id=id)

    # Find all associated sedimentary stratigraphic units
    sedimentaryues = UESedimentaria.objects.filter(hecho__id=id)

    # Find all associated built stratigraphic units
    builtues = UEConstruida.objects.filter(hecho__id=id)

    nombre = fact.letra + fact.numero
    data = { 'sedimentaryues': sedimentaryues, 'builtues': builtues, 'n_hecho': nombre}

    return render(request, 'excavationues.html', data)

# ######################
# Django authentication
# ######################
def register(request):
    # Get the fields of the registration form
    data = { 'form': UserCreationForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = UserCreationForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
        else:
            data['form'] = form

    return render(request, 'registration/register.html', data)


def send_email(request):
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
            template = get_template('registration/password_reset_email.html')
            content = template.render(data)

            msg2 = EmailMultiAlternatives

            msg = EmailMultiAlternatives(
                    subject='MyFindings: restablecer contraseña',
                    from_email=settings.EMAIL_HOST_USER,
                    to=[user.email])

            msg.attach_alternative(content, "text/html")
            msg.send()

            return redirect(to='password_reset_done')
        else:
            data['form'] = form

    return redirect(to='password_reset', context=data)
