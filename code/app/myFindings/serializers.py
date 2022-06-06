from rest_framework import serializers
from .models import BuiltMaterial, BuiltUE, Excavation, Fact, Inclusion, \
                    Photo, Room, SedimentaryMaterial, SedimentaryUE

class ExcavationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excavation
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):

    imagen_url = serializers.SerializerMethodField('get_imagen_url')

    class Meta:
        model = Photo
        fields = '__all__'

    def get_imagen_url(self, photo):
        if photo.imagen:
            return photo.imagen.url
        return ''

class InclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inclusion
        fields = '__all__'

class BuiltUESerializer(serializers.ModelSerializer):

    croquis_planta_url = serializers.SerializerMethodField('get_croquis_planta_url')
    croquis_seccion_url = serializers.SerializerMethodField('get_croquis_seccion_url')

    class Meta:
        model = BuiltUE
        fields = '__all__'

    def get_croquis_planta_url(self, builtue):
        if builtue.croquis_planta:
            return builtue.croquis_planta.url
        return ''

    def get_croquis_seccion_url(self, builtue):
        if builtue.croquis_seccion:
            return builtue.croquis_seccion.url
        return ''

class SedimentaryUESerializer(serializers.ModelSerializer):

    croquis_planta_url = serializers.SerializerMethodField('get_croquis_planta_url')
    croquis_seccion_url = serializers.SerializerMethodField('get_croquis_seccion_url')

    class Meta:
        model = SedimentaryUE
        fields = '__all__'

    def get_croquis_planta_url(self, sedimentaryue):
        if sedimentaryue.croquis_planta:
            return sedimentaryue.croquis_planta.url
        return ''

    def get_croquis_seccion_url(self, sedimentaryue):
        if sedimentaryue.croquis_seccion:
            return sedimentaryue.croquis_seccion.url
        return ''

class BuiltMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuiltMaterial
        fields = '__all__'

class SedimentaryMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedimentaryMaterial
        fields = '__all__'

class FactSerializer(serializers.ModelSerializer):

    croquis_plan_url = serializers.SerializerMethodField('get_croquis_plan_url')
    croquis_seccion_url = serializers.SerializerMethodField('get_croquis_seccion_url')

    class Meta:
        model = Fact
        fields = '__all__'

    def get_croquis_plan_url(self, fact):
        if fact.croquis_plan:
            return fact.croquis_plan.url
        return ''

    def get_croquis_seccion_url(self, fact):
        if fact.croquis_seccion:
            return fact.croquis_seccion.url
        return ''

class RoomSerializer(serializers.ModelSerializer):

    croquis_planta_url = serializers.SerializerMethodField('get_croquis_planta_url')

    class Meta:
        model = Room
        fields = '__all__'

    def get_croquis_planta_url(self, room):
        if room.croquis_planta:
            return room.croquis_planta.url
        return ''
