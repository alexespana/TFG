from django.contrib import admin
from .models import Estancia, Excavacion, Fotografia, Hecho, Inclusion, MaterialConstruida, MaterialSedimentaria, UEConstruida, UESedimentaria

# Register your models here.
@admin.register(Estancia)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('n_estancia', 'n_zona', 'n_sector', 'fase', 'periodo')
    search_fields = ('n_estancia', 'n_zona', 'n_sector')
    ordering = ('n_estancia',)
    list_per_page = 10

@admin.register(Hecho)  # This decorator registers the model in the admin interface
class FactAdmin(admin.ModelAdmin):
    list_display = ('letra', 'numero')
    ordering = ('letra','numero',)
    list_filter = ('estancia',)
    list_per_page = 10

@admin.register(Excavacion)
class ExcavationAdmin(admin.ModelAdmin):
    list_display = ('n_excavacion', 'latitud', 'longitud', 'altura')
    search_fields = ('n_excavacion', 'latitud', 'longitud', 'altura')
    ordering = ('n_excavacion',)
    list_per_page = 10

@admin.register(Fotografia)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ue', 'estancia')
    search_fields = ('numero','ue__codigo', 'estancia__n_estancia')
    list_filter = ('ue', 'estancia')
    list_per_page = 10

@admin.register(MaterialConstruida)
class BuiltMaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(MaterialSedimentaria)
class SedimentaryMaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_per_page = 10

@admin.register(UEConstruida, UESedimentaria)
class UEAdmin(admin.ModelAdmin):
    list_display = ('codigo','excavacion')
    search_fields = ('codigo','excavacion__n_excavacion')
    ordering = ('codigo',)
    list_filter = ('excavacion','hecho')
    list_per_page = 10

@admin.register(Inclusion)
class InclusionAdmin(admin.ModelAdmin):
    list_display = ('tipo','uesedimentaria','frecuencia', 'grosor')
    search_fields = ('tipo','uesedimentaria__codigo','frecuencia', 'grosor')
    ordering = ('tipo','uesedimentaria__codigo')
    list_filter = ('uesedimentaria',)
    list_per_page = 10


# Changing the header, title and description of the admin interface
admin.site.index_title = 'MyFindings'
