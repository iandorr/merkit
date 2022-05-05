from django.db import models

from filer.fields.image import FilerImageField

from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PlaceholderField

from tinymce.models import HTMLField

# Create your models here.

class WelcomeModel(CMSPlugin):
    welcome_text = models.CharField(max_length=255,default="Vítejte na Merkit",help_text="Hlavní uvítací text.")

class MainInfoModel(CMSPlugin):
    title = models.CharField(max_length=64,default="Hlavní Informace",help_text="Titulek hlavní info sekce.")
    text = models.TextField(help_text="Text zobrazený v hlavní info sekce.")

class ServicesModel(CMSPlugin):
    title = models.CharField(max_length=64,default="Služby",help_text="Titulek služeb.")

class ServiceModel(CMSPlugin):

    name = models.CharField(max_length=64,help_text="Rozeznávací jméno služby, musí být unikátní.")

    title = models.CharField(max_length=64,help_text="Titul služby.")
    #image = FilerImageField()
    image = models.ImageField(upload_to='images/')
    back_title = models.CharField(max_length=64,help_text="Titul služby na zadní straně karty.")
    back_text = models.TextField(help_text="Text na zadní straně karty.")

    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ServiceDetailModel(CMSPlugin):

    title = models.CharField(max_length=64,help_text="Titulek detailu služeb.")
    text = models.TextField(help_text="Text popisující službu.")
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')

    references = HTMLField()


class ContactFormModel(CMSPlugin):
    title = models.CharField(max_length=64,default="Kontakt",help_text="Titulek formuláře kontaktu.")
    text = models.TextField(help_text="Text zobrazený pod titulkem.",blank=True)

    email_label = models.CharField(max_length=32,default="Email",help_text="Popis pole pro zadání emailu.")
    name_label = models.CharField(max_length=32,default="Jméno",help_text="Popis pole pro zadání křestního jména.")
    surname_label = models.CharField(max_length=32,default="Příjmení",help_text="Popis pole pro zadání příjmení.")
    phone_label = models.CharField(max_length=32,default="Telefonní číslo",help_text="Popis pole pro zadání telefonního čísla.")
    subject_label = models.CharField(max_length=32,default="Předmět",help_text="Popis pole pro zadání předmětu.")
    message_label = models.CharField(max_length=32,default="Zpráva",help_text="Popis pole pro zadání těla zprávy.")

    confirmation = models.TextField(help_text="Souhlas s podmínkami.",blank=True)