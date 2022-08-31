
from dynamic_preferences.preferences import Section
from dynamic_preferences.types import StringPreference
from dynamic_preferences.registries import global_preferences_registry

from django.conf import settings

general = Section('general')

@global_preferences_registry.register
class EmailHostUser(StringPreference):

    section = general
    name = 'EMAIL_HOST_USER'
    default = settings.EMAIL_HOST_USER
    required = True

    verbose_name = 'Host Email'