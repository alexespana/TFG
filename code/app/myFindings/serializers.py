from rest_framework import serializers
from .models import BuiltMaterial, BuiltUE, Excavation, Fact, Inclusion, \
                    Photo, Room, SedimentaryMaterial, SedimentaryUE

class ExcavationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excavation
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class InclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inclusion
        fields = '__all__'

class BuiltUESerializer(serializers.ModelSerializer):
    class Meta:
        model = BuiltUE
        fields = '__all__'

class SedimentaryUESerializer(serializers.ModelSerializer):
    class Meta:
        model = SedimentaryUE
        fields = '__all__'

class BuiltMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuiltMaterial
        fields = '__all__'

class SedimentaryMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedimentaryMaterial
        fields = '__all__'

class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = '__all__'

class FactPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ['croquis_plan']

class FactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ['croquis_seccion']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['croquis_planta']

class SedimentaryUEFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedimentaryUE
        fields = ['croquis_planta']

class SedimentaryUESectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedimentaryUE
        fields = ['croquis_seccion']

class BuiltUEFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuiltUE
        fields = ['croquis_planta']

class BuiltUESectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuiltUE
        fields = ['croquis_seccion']
