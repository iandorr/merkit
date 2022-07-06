from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language

from cms.models.pagemodel import Page

from plugins_app.models import WelcomeModel,MainInfoModel,ContactFormModel, ServicesModel, ServiceModel, ServiceDetailModel, LinkManager
from plugins_app.forms import ContactPluginForm, SubmitContactForm, ServiceForm

@plugin_pool.register_plugin
class NavLinkPlugin(CMSPluginBase):
    render_template = "navbar_plugin.html"
    cache = False

    def render(self,context,instance,placeholder):

        unsorted_links = []

        page_id = instance.placeholder.page.id
        page = Page.objects.get(id = page_id)

        placeholders = page.placeholders.all()

        for placeholder in placeholders:
            if placeholder.slot == 'content':
                break

        plugins = placeholder.get_plugins(language=get_language())

        link_manager = LinkManager.objects.all()[0]
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
class WelcomePlugin(CMSPluginBase):
    model = WelcomeModel
    render_template = "welcome_plugin.html"
    cache = False

@plugin_pool.register_plugin
class MainInfoPlugin(CMSPluginBase):
    model = MainInfoModel
    render_template = "main_info_plugin.html"
    cache = False

@plugin_pool.register_plugin
class ContactFormPlugin(CMSPluginBase):
    model = ContactFormModel
    form = ContactPluginForm
    render_template = "contact_form_plugin.html"
    cache = False

    def render(self,context,instance,placeholder):

        request = context['request']

        if request.method == "POST":
            if 'contact_submit' in request.POST:
                submit_form = SubmitContactForm(request.POST)
                # TODO: send mail using the custom server ... smt like send_mail(), mail server not set up
                if submit_form.is_valid():
                    print("Human")
                else:
                    print("Bot")

                # context.update({
                #     'form':form
                # })

                # context['instance'] = instance
                # context['placeholder'] = placeholder
                # return context

        submit_form = SubmitContactForm()
        context.update({
            'form': submit_form
        })

        context['instance'] = instance
        context['placeholder'] = placeholder
        return context


@plugin_pool.register_plugin
class ServicesPlugin(CMSPluginBase):
    model = ServicesModel
    render_template = "services_list_plugin.html"
    allow_children = True
    child_classes = ['ServicePlugin']
    cache = False

    def render(self,context,instance,placeholder):

        # pages = Page.objects.public()
        # for page in pages:
        #     print(page.get_public_url())

        request = context['request']
        if request.method == "POST":
            if 'plugin_select' in request.POST:
                selected = request.POST.getlist('plugin_select')
                if len(selected) == 3:
                    previouse_pks = ServiceModel.objects.filter(featured=True)
                    for prev_pk in previouse_pks:
                        prev_pk.featured = False
                        prev_pk.save()

                    for item in selected:
                        new = ServiceModel.objects.get(pk=item)
                        new.featured = True
                        new.save()
                        all_new = ServiceModel.objects.filter(name=new.name)
                        if len(all_new) == 2:
                            for candidate in all_new:
                                if candidate.pk != new.pk:
                                    candidate.featured = True
                                    candidate.save()

                        else:
                            #TODO: manage if somehow there are more ... maybe sort them using pks and make twos ... + add some string to them (self.name)
                            pass

        instance_pks = []
        for plugin in instance.child_plugin_instances:
            instance_pks.append(plugin.pk)

        all_instance_plugins = ServiceModel.objects.filter(pk__in=instance_pks)

        service_plugins = ServiceModel.objects.filter(featured=True,pk__in=instance_pks)

        detail_plugins = ServiceDetailModel.objects.all()
        rendered_details = []

        for detail in detail_plugins:
            for plugin in service_plugins:
                if detail.parent.pk == plugin.pk:
                    rendered_details.append(detail)
                    break

        context = super().render(context, instance, placeholder)

        context.update({
            'rendered_plugins': service_plugins,
            'rendered_details': rendered_details,
            'instance_plugins': all_instance_plugins
        })

        return context

@plugin_pool.register_plugin
class ServicePlugin(CMSPluginBase):
    render_template = 'service_plugin.html'
    model = ServiceModel
    form = ServiceForm
    require_parent = True
    parent_classes = ['ServicesPlugin']
    allow_children = True
    child_classes = ['ServiceDetailPlugin']

    def render(self, context, instance, placeholder):
        context = super(ServicePlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ServiceDetailPlugin(CMSPluginBase):
    render_template = 'service_detail_plugin.html'
    model = ServiceDetailModel
    require_parent = True
    parent_classes = ['ServicePlugin']

    def render(self, context, instance, placeholder):
        context = super(ServiceDetailPlugin, self).render(context, instance, placeholder)
        return context