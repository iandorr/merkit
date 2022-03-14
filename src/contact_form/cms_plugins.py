
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .forms import SubmitContactForm
from django.core.mail import send_mail

from dynamic_preferences.registries import global_preferences_registry

@plugin_pool.register_plugin
class ContactFormPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "contact_form.html"
    cache = False

    def render(self,context,instance,placeholder):

        request = context['request']

        if request.method == "POST":
            form = SubmitContactForm(request.POST)
            #TODO do smt with form
        else:
            form = SubmitContactForm()
            context.update({
                'form': form
            })
        return context