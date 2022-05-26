from django.contrib import admin
from .models import Room, Excavation, Photo, Fact, Inclusion, BuiltMaterial, SedimentaryMaterial, BuiltUE, SedimentaryUE

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('n_estancia', 'n_zona', 'n_sector', 'fase', 'periodo')
    search_fields = ('n_estancia', 'n_zona', 'n_sector')
    ordering = ('n_estancia',)
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['n_estancia']
        else:
            return []

@admin.register(Fact)  # This decorator registers the model in the admin interface
class FactAdmin(admin.ModelAdmin):
    list_display = ('letra', 'numero')
    ordering = ('letra','numero',)
    list_filter = ('estancia',)
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['letra', 'numero']
        else:
            return []

@admin.register(Excavation)
class ExcavationAdmin(admin.ModelAdmin):
    list_display = ('nombre','n_excavacion', 'latitud', 'longitud', 'altura')
    search_fields = ('nombre','n_excavacion', 'latitud', 'longitud', 'altura')
    ordering = ('n_excavacion',)
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['n_excavacion']
        else:
            return []

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ue', 'estancia')
    search_fields = ('numero','ue__codigo', 'estancia__n_estancia')
    list_filter = ('ue', 'estancia')
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['numero']
        else:
            return []

@admin.register(BuiltMaterial)
class BuiltMaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['nombre']
        else:
            return []

@admin.register(SedimentaryMaterial)
class SedimentaryMaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['nombre']
        else:
            return []

@admin.register(BuiltUE, SedimentaryUE)
class UEAdmin(admin.ModelAdmin):
    list_display = ('codigo','excavacion')
    search_fields = ('codigo','excavacion__n_excavacion')
    ordering = ('codigo',)
    list_filter = ('excavacion','hecho')
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['codigo', 'excavacion', 'n_orden']
        else:
            return ['codigo']

@admin.register(Inclusion)
class InclusionAdmin(admin.ModelAdmin):
    list_display = ('tipo','uesedimentaria','frecuencia', 'grosor')
    search_fields = ('tipo','uesedimentaria__codigo','frecuencia', 'grosor')
    ordering = ('tipo','uesedimentaria__codigo')
    list_filter = ('uesedimentaria',)
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['tipo', 'uesedimentaria']
        else:
            return []

# Changing the header, title and description of the admin interface
admin.site.index_title = 'MyFindings'
