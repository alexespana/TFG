
from django import forms
from .models import Room, Excavation, Inclusion, Photo, Fact, BuiltMaterial, SedimentaryMaterial, \
                    BuiltUE, SedimentaryUE
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
        exclude = ['codigo', 'cota_superior', 'cota_inferior']

class BuiltUEForm(forms.ModelForm):
    class Meta:
        model = BuiltUE
        fields = '__all__'
        exclude = ['codigo', 'cota_superior', 'cota_inferior']

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
    email = forms.EmailField(label='Correo electrónico', required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserChangeForm(forms.ModelForm):
    # Name and email of the user must be disabled
    username = forms.CharField(label='Nombre de usuario', required=False, disabled=True)
    email = forms.EmailField(label='Correo electrónico', required=False, disabled=True)
    is_active = forms.BooleanField(label='Activo', required=False, help_text='Activa o desactiva la cuenta del usuario.')

    class Meta:
        model = User
        # I need only the username, email, is_active and groups
        fields = ['username', 'email', 'is_active', 'groups']

class InclusionUpdateForm(forms.ModelForm):
    # Tipo and uesedimentaria must be disabled
    tipo = forms.ChoiceField(label='Tipo', required=False, disabled=True, choices=Inclusion.TIPO_CHOICES)
    uesedimentaria = forms.ModelChoiceField(label='UE Sedimentaria', required=False, disabled=True, queryset=SedimentaryUE.objects.all())

    class Meta:
        model = Inclusion
        fields = '__all__'

class FactUpdateForm(forms.ModelForm):
    # Letra and numero must be disabled
    letra = forms.ChoiceField(label='Letra', required=False, disabled=True, choices=Fact.LETRA_CHOICES)
    numero = forms.IntegerField(label='Número', required=False, disabled=True)

    class Meta:
        model = Fact
        fields = '__all__'

class SedimentaryUEUpdateForm(forms.ModelForm):
    # Excavacion must be disabled
    excavacion = forms.ModelChoiceField(label='Excavación', required=False, disabled=True, to_field_name='n_excavacion', queryset=Excavation.objects.all())
    
    # Make the field n_orden readonly in the __init__ method because validation in models.py is not working
    def __init__(self, *args, **kwargs):
        super(SedimentaryUEUpdateForm, self).__init__(*args, **kwargs)
        self.fields['n_orden'].widget.attrs['readonly'] = True

    class Meta:
        model = SedimentaryUE
        fields = '__all__'
        exclude = ['codigo', 'cota_superior', 'cota_inferior']

class BuiltUEUpdateForm(forms.ModelForm):
    # Excavacion and n_orden must be disabled
    excavacion = forms.ModelChoiceField(label='Excavación', required=False, disabled=True, to_field_name='n_excavacion' ,queryset=Excavation.objects.all())

    # Make the field n_orden readonly in the __init__ method because validation in models.py is not working
    def __init__(self, *args, **kwargs):
        super(BuiltUEUpdateForm, self).__init__(*args, **kwargs)
        self.fields['n_orden'].widget.attrs['readonly'] = True

    class Meta:
        model = BuiltUE
        fields = '__all__'
        exclude = ['codigo', 'cota_superior', 'cota_inferior']
