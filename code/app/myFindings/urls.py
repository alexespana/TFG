# myFindings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='home'),
    # Sobre la aplicación
    path('about/', views.about, name='about'),
    # Contacto
    path('contact/', views.contact, name='contact'),
    # Equipo
    path('team/', views.team, name='team'),

    # ############
    # EXCAVATIONS
    # ############
    # Excavations list
    path('excavations_list/', views.list_excavations, name="excavations_list"),
    # Add excavacion
    path('add_excavation/', views.add_excavation, name='add_excavation'),
    # Modify excavation
    path('modify_excavation/<id>/', views.modify_excavation, name="modify_excavation"),
    # Delete excavation
    path('delete_excavation/<id>/', views.delete_excavation, name="delete_excavation"),

    # ################
    # SEDIMENTARY UE
    # ################
    # Sedimentary UES list
    path('sedimentaryues_list/', views.list_sedimentaryues, name='sedimentaryues_list'),
    # Add sedimentary UE
    path('add_sedimentaryue/', views.add_sedimentaryue, name='add_sedimentaryue'),
    # Modify sedimentaryue
    path('modify_sedimentaryue/<id>/', views.modify_sedimentaryue, name="modify_sedimentaryue"),
  # Delete sedimentaryue
    path('delete_sedimentaryue/<id>/', views.delete_sedimentaryue, name="delete_sedimentaryue"),

    # ################
    # BUILT UE
    # ################
    # Built UES list
    path('builtues_list/', views.list_builtues, name='builtues_list'),
    # Add built UE
    path('add_builtue/', views.add_builtue, name='add_builtue'),
    # Modify built UE
    path('modify_builtue/<id>/', views.modify_builtue, name="modify_builtue"),
  # Delete built UE
    path('delete_builtue/<id>/', views.delete_builtue, name="delete_builtue"),

    # ################
    # FACT
    # ################
    # Built UE list
    path('facts_list/', views.list_facts, name='facts_list'),
    # Add biult UE
    path('add_fact/', views.add_fact, name='add_fact'),
    # Modify sedimentaryue
    path('modify_fact/<id>/', views.modify_fact, name="modify_fact"),
    # Delete fact
    path('delete_fact/<id>/', views.delete_fact, name="delete_fact"),

    # ################
    # ROOM
    # ################
    # Rooms list
    path('rooms_list/', views.list_rooms, name='rooms_list'),
    # Add room
    path('add_room/', views.add_room, name='add_room'),
    # Modify room
    path('modify_room/<id>/', views.modify_room, name="modify_room"),
    # Delete room
    path('delete_room/<id>/', views.delete_room, name="delete_room"),


    # ################
    # PHOTO
    # ################
    # Photos list
    path('photos_list/', views.list_photos, name='photos_list'),
    # Add photo
    path('add_photo/', views.add_photo, name='add_photo'),
    # Modify photo
    path('modify_photo/<id>/', views.modify_photo, name="modify_photo"),
    # Delete photo
    path('delete_photo/<id>/', views.delete_photo, name="delete_photo"),



    # ################
    # INCLUSION
    # ################
    # Inclusions list
    path('inclusions_list/', views.list_inclusions, name='inclusions_list'),
    # Add inclusion
    path('add_inclusion/', views.add_inclusion, name='add_inclusion'),
    # Modify inclusion
    path('modify_inclusion/<id>/', views.modify_inclusion, name="modify_inclusion"),
    # Delete photo
    path('delete_inclusion/<id>/', views.delete_inclusion, name="delete_inclusion"),

    # #####################
    # SEDIMENTARY MATERIAL
    # #####################
    # Sedimentary materials list
    path('sedimentarymaterials_list/', views.list_sedimentarymaterials, name='sedimentarymaterials_list'),
    # Add sedimentary material
    path('add_sedimentarymaterial/', views.add_sedimentarymaterial, name='add_sedimentarymaterial'),
    # Modify sedimentary material
    path('modify_sedimentarymaterial/<id>/', views.modify_sedimentarymaterial, name="modify_sedimentarymaterial"),
    # Delete sedimentary material
    path('delete_sedimentarymaterial/<nombre>/', views.delete_sedimentarymaterial, name="delete_sedimentarymaterial"),

    # #####################
    # BUILT MATERIAL
    # #####################
    # Built materials list
    path('builtmaterials_list/', views.list_builtmaterials, name='builtmaterials_list'),
    # Add built material
    path('add_builtmaterial/', views.add_builtmaterial, name='add_builtmaterial'),
    # Modify built material
    path('modify_builtmaterial/<id>/', views.modify_builtmaterial, name="modify_builtmaterial"),
    # Delete built material
    path('delete_builtmaterial/<nombre>/', views.delete_builtmaterial, name="delete_builtmaterial"),

]