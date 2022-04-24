from django import forms
from .models import Room, Excavation, Inclusion, Photo, Fact, BuiltMaterial, SedimentaryMaterial, BuiltUE, SedimentaryUE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExcavationForm(forms.ModelForm):
    class Meta:
        model = Excavation
        fields = '__all__'

class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class SedimentaryUEForm(forms.ModelForm):
    class Meta:
        model = SedimentaryUE
        fields = '__all__'

class BuiltUEForm(forms.ModelForm):
    class Meta:
        model = BuiltUE
        fields = '__all__'

class SedimentaryMaterialForm(forms.ModelForm):
    class Meta:
        model = SedimentaryMaterial
        fields = '__all__'

class BuiltMaterialForm(forms.ModelForm):
    class Meta:
        model = BuiltMaterial
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