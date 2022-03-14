from django.shortcuts import render, redirect, get_object_or_404
from .forms import BuiltMaterialForm, BuiltUEForm, ExcavationForm, FactForm, InclusionForm, RoomForm, SedimentaryMaterialForm, SedimentaryUEForm, PhotoForm
from .models import Excavacion, Fotografia, Hecho, Estancia, Inclusion, MaterialConstruida, MaterialSedimentaria, UEConstruida, UESedimentaria

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
def list_excavations(request):
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
            return redirect(to='excavations_list')
        else:
            data['form'] = form

    return render(request, 'add_excavation.html', data)

def modify_excavation(request):
    pass

def delete_excavation(request, id):
    # Get the excavation, if it doesn't exist, get an Http404
    excavation = get_object_or_404(Excavacion, id=id)

    # Delete the excavation
    excavation.delete()    

    return redirect(to="excavations_list")    

# ################
# SEDIMENTARY UE
# ################
def list_sedimentaryues(request):
    # Get all sedimentary ues
    sedimentaryues = UESedimentaria.objects.all()
    data = { 'sedimentaryues': sedimentaryues}

    return render(request, 'sedimentaryues_list.html', data)

def add_sedimentaryue(request):
    # Get the fields of the sedimentary ue
    data = { 'form': SedimentaryUEForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = SedimentaryUEForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of excavations
            return redirect(to='sedimentaryues_list')
        else:
            data['form'] = form

    return render(request, 'add_sedimentaryue.html', data)

def modify_sedimentaryue(request):
    pass

def delete_sedimentaryue(request):
    # Get the sedimentary ue, if it doesn't exist, get an Http404
    sedimentaryue = get_object_or_404(UESedimentaria, id=id)

    # Delete the excavation
    sedimentaryue.delete()    

    return redirect(to="sedimentaryues_list")   

# ################
# BUILT UE
# ################
def list_builtues(request):
    # Get all built ues
    builtues = UEConstruida.objects.all()
    data = { 'builtues': builtues}

    return render(request, 'builtues_list.html', data)

def add_builtue(request):
    # Get the fields of built ue
    data = { 'form': BuiltUEForm() }

    if request.method == 'POST':
        # Get the data entered by the user
        form = BuiltUEForm(data=request.POST)
        if(form.is_valid()):    # Check if valid
            form.save()         # Save form

            # Redirect to the list of excavations
            return redirect(to='builtues_list')
        else:
            data['form'] = form

    return render(request, 'add_builtue.html', data)

def modify_builtue(request):
    pass

def delete_builtue(request):
    # Get the sedimentary ue, if it doesn't exist, get an Http404
    builtue = get_object_or_404(UEConstruida, id=id)

    # Delete the excavation
    builtue.delete()    

    return redirect(to="builtues_list")


# ################
# FACT
# ################
def list_facts(request):
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
            return redirect(to='facts_list')
        else:
            data['form'] = form

    return render(request, 'add_fact.html', data)

def modify_fact(request):
    pass

def delete_fact(request, id):
    # Get the fact, if it doesn't exist, get an Http404
    fact = get_object_or_404(Hecho, id=id)

    # Delete the excavation
    fact.delete()    

    return redirect(to="facts_list")  

# ################
# ROOM
# ################
def list_rooms(request):
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
            return redirect(to='rooms_list')
        else:
            data['form'] = form

    return render(request, 'add_room.html', data) 

def modify_room(request):
    pass

def delete_room(request, id):
    # Get the room, if it doesn't exist, get an Http404
    room = get_object_or_404(Estancia, id=id)

    # Delete the room
    room.delete()    

    return redirect(to="rooms_list") 

# ################
# PHOTO
# ################
def list_photos(request):
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
            return redirect(to='photos_list')
        else:
            data['form'] = form

    return render(request, 'add_photo.html', data)

def modify_photo(request):
    pass
 
def delete_photo(request, id):
    # Get the photo, if it doesn't exist, get an Http404
    photo = get_object_or_404(Fotografia, id=id)

    # Delete the photo
    photo.delete()    

    return redirect(to="photos_list") 

# ################
# INCLUSION
# ################
def list_inclusions(request):
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
            return redirect(to='inclusions_list')
        else:
            data['form'] = form

    return render(request, 'add_inclusion.html', data)


def modify_inclusion(request):
    pass

def delete_inclusion(request, id):
    # Get the inclusion, if it doesn't exist, get an Http404
    inclusion = get_object_or_404(Inclusion, id=id)

    # Delete the inclusion
    inclusion.delete()    

    return redirect(to="inclusions_list")

# #####################
# SEDIMENTARY MATERIAL
# #####################
def list_sedimentarymaterials(request):
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
            return redirect(to='sedimentarymaterials_list')
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

    return redirect(to="sedimentarymaterials_list")

# #####################
# BUILT MATERIAL
# #####################
def list_builtmaterials(request):
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
            return redirect(to='builtmaterials_list')
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

    return redirect(to="builtmaterials_list")
