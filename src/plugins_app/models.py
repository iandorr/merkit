from django.db import models

from filer.fields.image import FilerImageField

from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PlaceholderField

from tinymce.models import HTMLField

from cms.models.pagemodel import Page

from django.utils.translation import gettext_lazy as _



# Create your models here.

class LinkManager(models.Model):
    
    def __str__(self):
        return "Link Manager"

class MerkitNavbarModel(CMSPlugin):

    logo = models.ImageField(upload_to='images/')

class DefaultPluginModel(CMSPlugin):

    show_link = models.BooleanField(default=False, help_text=_("If selected, the link will be shown in the Nav Link Plugin."))
    link_title = models.CharField(max_length=64, blank=True, help_text=_("Title that will be shown in Nav Link Plugin."))
    link_href = models.CharField(max_length=64, blank=True, help_text=_("ID that will be appended to the section, create a unique one please."))
    link_manager = models.ForeignKey(LinkManager,null=True,on_delete=models.SET_NULL,help_text=_("Please select Link Manager."))

    class Meta:
        abstract = True

    def save(self, no_signals=False, *args, **kwargs):

        managers = LinkManager.objects.all().order_by('pk')

        if not managers.exists():
            link_manager = LinkManager(number=1)
            link_manager.save()

        for i in range(1,len(managers)):
            managers[i].delete()

        link_manager = managers[0]

        if self.link_manager == None:
            self.link_manager = link_manager
            self.save()


        if not self.depth:
            if self.parent_id or self.parent:
                self.parent.add_child(instance=self)
            else:
                if not self.position and not self.position == 0:
                    self.position = CMSPlugin.objects.filter(parent__isnull=True,
                                                             language=self.language,
                                                             placeholder_id=self.placeholder_id).count()
                self.add_root(instance=self)
            return
        super().save(*args, **kwargs)

class WelcomeModel(DefaultPluginModel):
    welcome_text = models.CharField(max_length=255,default="Vítejte na Merkit",help_text=_("Main welcome text."))

class MainInfoModel(DefaultPluginModel):
    title = models.CharField(max_length=64,default="Hlavní Informace",help_text=_("Title of the main info section."))
    text = models.TextField(help_text=_("Text showcased in the main info section."))

class ServicesModel(DefaultPluginModel):
    title = models.CharField(max_length=64,default="Služby",help_text=_("Title of the services section."))

class ServiceModel(CMSPlugin):

    name = models.CharField(max_length=64,help_text=_("Discerning name of the service, must be unique!"))

    title = models.CharField(max_length=64,help_text=_("Title of the service."))
    #image = FilerImageField()
    image = models.ImageField(upload_to='images/')
    back_title = models.CharField(max_length=64,help_text=_("Title of the service on the back of the card."))
    back_text = models.TextField(help_text=_("Text on the back of the card."))

    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ServiceDetailModel(CMSPlugin):

    title = models.CharField(max_length=64,help_text=_("Title of the service detail."))
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')


class ContactFormModel(DefaultPluginModel):
    title = models.CharField(max_length=64,default="Kontakt",help_text=_("Title of the contact form."))
    text = models.TextField(help_text=_("Text showcased under the title on the contact form."),blank=True)

    confirmation = models.TextField(help_text=_("Agreement with the terms."),blank=True)