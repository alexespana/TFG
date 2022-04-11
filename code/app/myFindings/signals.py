from .views import send_email
from django.conf import settings
from django.contrib.auth.models import User

def active(sender, instance, **kwargs):
    if instance.is_active and User.objects.filter(pk=instance.pk, is_active=False).exists():
        data = { 'user': instance}
        send_email(subject='MyFindings: cuenta activada', from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[instance.email], html_message='registration/account_activated.html', data=data)

def register(sender, instance, **kwargs):
    if kwargs.get('created', False):
        data = { 'user': instance}
        send_email(subject='Verificación de registro', from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER], html_message='registration/registration_check.html', data=data)        
