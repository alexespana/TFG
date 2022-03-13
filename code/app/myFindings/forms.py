from django import forms
from .models import Estancia, Excavacion, Fotografia, Hecho, Inclusion, MaterialConstruida, MaterialSedimentaria, UEConstruida, UESedimentaria

class ExcavationForm(forms.ModelForm):
    class Meta:
        model = Excavacion
        fields = '__all__'

class FactForm(forms.ModelForm):
    class Meta:
        model = Hecho
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Estancia
        fields = '__all__'

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        fields = '__all__'

class SedimentaryUEForm(forms.ModelForm):
    class Meta:
        model = UESedimentaria
        fields = '__all__'

class BuiltUEForm(forms.ModelForm):
    class Meta:
        model = UEConstruida
        fields = '__all__'

class SedimentaryMaterialForm(forms.ModelForm):
    class Meta:
        model = MaterialSedimentaria
        fields = '__all__'

class BuiltMaterialForm(forms.ModelForm):
    class Meta:
        model = MaterialConstruida
        fields = '__all__'

class InclusionForm(forms.ModelForm):
    class Meta:
        model = Inclusion
        fields = '__all__'
