
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from django.core.mail import send_mail

from dynamic_preferences.registries import global_preferences_registry

@plugin_pool.register_plugin
class ContactSubmitPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "contact_submit.html"
    cache = False

    def render(self,context,instance,placeholder):

        if ('contact_submit' in context['request'].GET):
            data = context['request'].GET

            global_preferences = global_preferences_registry.manager()

            send_mail(
                data['subject'], # subject
                data['message'], # message
                data['mail'], # from
                ['hortensky.jakub@gmail.com'], # to
                False, # fail_silently
                global_preferences['general__EMAIL_HOST_USER'], # auth-user
                global_preferences['general__EMAIL_HOST_PASSWORD'], # auth-password
            )

            print('Mail Sent')