from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from cms.models.pagemodel import Page

from plugins_app.models import WelcomeModel,MainInfoModel,ContactFormModel, ServicesModel, ServiceModel, ServiceDetailModel, LinkModel
from plugins_app.forms import SubmitContactForm, ServiceForm


@plugin_pool.register_plugin
class NavLinkPlugin(CMSPluginBase):
    render_template = "navlink_plugin.html"
    cache = False
    allow_children = True
    child_classes = ['LinkPlugin']

@plugin_pool.register_plugin
class LinkPlugin(CMSPluginBase):
    model = LinkModel
    render_template = "link_plugin.html"
    cache = False
    require_parent = True
    parent_classes = ['NavLinkPlugin']


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
    render_template = "contact_form_plugin.html"
    cache = False

    def render(self,context,instance,placeholder):

        request = context['request']

        if request.method == "POST":
            if 'contact_submit' in request.POST:
                form = SubmitContactForm(request.POST)
                # TODO: send mail using the custom server ... smt like send_mail(), mail server not set up
                if form.is_valid():
                    print("Human")
                else:
                    print("Bot")

                # context.update({
                #     'form':form
                # })

                # context['instance'] = instance
                # context['placeholder'] = placeholder
                # return context

        form = SubmitContactForm()
        context.update({
            'form': form
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