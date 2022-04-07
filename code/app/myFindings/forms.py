from django import forms
from .models import Estancia, Excavacion, Inclusion, Fotografia, Hecho, MaterialConstruida, MaterialSedimentaria, UEConstruida, UESedimentaria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']