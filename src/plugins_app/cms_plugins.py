from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


from cms.models.pagemodel import Page
from dynamic_preferences.registries import global_preferences_registry

from plugins_app.models import WelcomeModel,MainInfoModel,ContactFormModel, ServicesModel, ServiceModel, ServiceDetailModel, MerkitNavbarModel
from plugins_app.forms import SubmitContactForm, ServiceForm, WelcomeForm, MainInfoForm, ServiceListForm, ContactForm
from plugins_app.utils import get_link_manager


@plugin_pool.register_plugin
class MerkitNavbarPlugin(CMSPluginBase):

    model = MerkitNavbarModel
    render_template = "merkit_navbar_plugin.html"
    allow_children = True
    child_classes = ['MerkitLinkPlugin']

@plugin_pool.register_plugin
class MerkitLinkPlugin(CMSPluginBase):
    render_template = "merkit_link_plugin.html"
    cache = False
    require_parent = True
    parent_classes = ['MerkitNavbarPlugin']

    def render(self,context,instance,placeholder):

        """ Modifies the rendering of Nav plugin, finds the links of all the sections and webpages that are to be shown. """

        unsorted_links = []

        page_id = instance.placeholder.page.id
        page = Page.objects.get(id = page_id)

        placeholders = page.placeholders.all()

        for placeholder in placeholders:
            if placeholder.slot == 'content':
                break

        if placeholder.slot != 'content':
            context['instance'] = instance
            context['placeholder'] = placeholder
            return context

        plugins = placeholder.get_plugins(language=get_language())

        link_manager = get_link_manager()
        
        for f in link_manager._meta.get_fields():
            if f.one_to_many:
                items = f.related_model.objects.all()
                for item in items:
                    for plugin in plugins:
                        if item.id == plugin.id:
                            if item.show_link:
                                unsorted_links.append(item)
                            break

        links = sorted(unsorted_links,key=lambda t: t.get_position_in_placeholder())

        current_draft = page.publisher_is_draft

        pages = Page.objects.exclude(id=page_id)
        page_links = []
        for p in pages:
            if (p.in_navigation and p.publisher_is_draft == current_draft):
                if (get_language() in p.get_languages()):
                    page_links.append(p)

        context.update({
            'links': links,
            'page_links':page_links
        })
        context['instance'] = instance
        context['placeholder'] = placeholder
        return context


@plugin_pool.register_plugin
class MerkitWelcomePlugin(CMSPluginBase):
    model = WelcomeModel
    form = WelcomeForm
    render_template = "merkit_welcome_plugin.html"
    cache = False

@plugin_pool.register_plugin
class MerkitMainInfoPlugin(CMSPluginBase):
    model = MainInfoModel
    form = MainInfoForm
    render_template = "merkit_main_info_plugin.html"
    cache = False

@plugin_pool.register_plugin
class MerkitContactFormPlugin(CMSPluginBase):
    model = ContactFormModel
    form = ContactForm
    render_template = "merkit_contact_form_plugin.html"
    cache = False

    def render(self,context,instance,placeholder):

        """ Modifies the rendering of the Contact plugin, handles the POST request of the form. """

        request = context['request']

        global_preferences = global_preferences_registry.manager()
        receive_email = global_preferences['general__EMAIL_HOST_USER']

        if receive_email == settings.EMAIL_HOST_USER:
            warning = _("Please set the receiving email! Default is set to ") + settings.EMAIL_HOST_USER
            messages.warning(request,warning)

        if request.method == "POST":
            if 'contact_submit' in request.POST:
                submit_form = SubmitContactForm(request.POST)
                if submit_form.is_valid():      # this func checks csrf, form validity and recaptcha
                    email = submit_form.cleaned_data['email']
                    first_name = submit_form.cleaned_data['first_name']
                    last_name = submit_form.cleaned_data['last_name']
                    country_code = submit_form.cleaned_data['country_code']
                    phone_number = submit_form.cleaned_data['phone_number']
                    subject = submit_form.cleaned_data['subject']
                    text = submit_form.cleaned_data['text']

                    html_string = render_to_string("mail_template.html",{'title':"Email from Merkit",'first_name':first_name,'last_name':last_name,'country_code':country_code,'phone_number':phone_number,'text':text,'email':email})
                    text_string = strip_tags(html_string)

                    email_class = EmailMultiAlternatives(subject,text_string,settings.EMAIL_HOST_USER,[receive_email])
                    email_class.send()

                    messages.success(request,(_("Message sent successfully!")))

                else:

                    messages.error(request,(_("Error, try to send again!")))

        submit_form = SubmitContactForm()
        context.update({
            'form': submit_form
        })

        context['instance'] = instance
        context['placeholder'] = placeholder
        return context


@plugin_pool.register_plugin
class MerkitServiceListPlugin(CMSPluginBase):
    model = ServicesModel
    form = ServiceListForm
    render_template = "merkit_service_list_plugin.html"
    allow_children = True
    child_classes = ['MerkitServicePlugin']
    cache = False

    def render(self,context,instance,placeholder):

        """ Modifies the rendering of Services plugin, shows only those that are chosen (3),
        manages the checkbox form to choose which are chosen and sticks them to the Service detail. """

        request = context['request']
        language = get_language()
        if request.method == "POST":
            if 'plugin_select' in request.POST:
                selected = request.POST.getlist('plugin_select')
                if len(selected) == 3:
                    previouse_pks = ServiceModel.objects.filter(featured=True,language=language)
                    # unfeatures all the plugins
                    for prev_pk in previouse_pks:
                        prev_pk.featured = False
                        prev_pk.save()

                    # features the new ones
                    for item in selected:
                        new = ServiceModel.objects.get(pk=item)
                        new.featured = True
                        new.save()
                        # gets both plugins (published and draft) and changes the published one according to the draft one
                        published_plugins = ServiceModel.objects.filter(name=new.name,language=language).exclude(pk=new.pk)


                        if len(published_plugins) != 0:     #if published one exists
                            if len(published_plugins) == 1:
                                for candidate in published_plugins:
                                    if candidate.pk != new.pk:
                                        candidate.featured = True
                                        candidate.save()

                            else:
                                # for now let the position in the placeholder be static
                                try_new = ServiceModel.objects.filter(name=new.name,language=language,position=new.position).exclude(pk=new.pk)[0]

                                try_new.featured = True
                                try_new.save()


        instance_pks = []
        for plugin in instance.child_plugin_instances:
            instance_pks.append(plugin.pk)

        all_instance_plugins = ServiceModel.objects.filter(pk__in=instance_pks)

        service_models = ServiceModel.objects.filter(featured=True,pk__in=instance_pks).order_by('position')
        service_plugins = []
        detail_plugins = []
        for plugin in instance.child_plugin_instances:
            if(len(list(filter(lambda x : x.pk == plugin.pk,service_models)))==1):
                service_plugins.append(plugin)
                for child in plugin.child_plugin_instances:
                    if child is not None:
                        detail_plugins.append(child)

        context = super().render(context, instance, placeholder)

        context.update({
            'rendered_plugins': service_plugins,
            #'rendered_details': rendered_details,
            'rendered_details': detail_plugins,
            'instance_plugins': all_instance_plugins
        })

        return context

@plugin_pool.register_plugin
class MerkitServicePlugin(CMSPluginBase):
    render_template = 'merkit_service_plugin.html'
    model = ServiceModel
    form = ServiceForm
    require_parent = True
    parent_classes = ['MerkitServiceListPlugin']
    allow_children = True
    child_classes = ['MerkitServiceDetailPlugin']

    def render(self, context, instance, placeholder):
        context = super(MerkitServicePlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class MerkitServiceDetailPlugin(CMSPluginBase):
    render_template = 'merkit_service_detail_plugin.html'
    model = ServiceDetailModel
    require_parent = True
    parent_classes = ['MerkitServicePlugin']
    allow_children = True
    child_classes = ['TextPlugin','Bootstrap4LinkPlugin','Bootstrap4ListGroupPlugin','Bootstrap4PicturePlugin']

    def render(self, context, instance, placeholder):
        context = super(MerkitServiceDetailPlugin, self).render(context, instance, placeholder)
        return context