
from dynamic_preferences.preferences import Section
from dynamic_preferences.types import StringPreference
from dynamic_preferences.registries import global_preferences_registry

general = Section('general')

@global_preferences_registry.register
class EmailHostUser(StringPreference):

    section = general
    name = 'EMAIL_HOST_USER'
    default = 'None'
    required = True

    verbose_name = 'Host Email'