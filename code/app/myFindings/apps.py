from django.apps import AppConfig
from django.db.models.signals import pre_save, post_save

class MyfindingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myFindings'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
        from django.contrib.auth.models import User

        pre_save.connect(signals.active, sender=User, dispatch_uid='active')
        post_save.connect(signals.register, sender=User, dispatch_uid='register')
