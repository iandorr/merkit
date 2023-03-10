from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.core.validators import EMPTY_VALUES
from django.utils.translation import gettext_lazy as _


from plugins_app.models import ContactFormModel, ServiceModel, WelcomeModel, MainInfoModel, ServicesModel
from plugins_app.utils import link_href_taken, service_name_taken

class SubmitContactForm(forms.Form):

    email = forms.EmailField(max_length=50,min_length=8,required=True,widget=forms.EmailInput(attrs={'placeholder':_("placeholder-email"),'id':'mail'}))
    first_name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':_("placeholder-name"),'id':'first-name','pattern':'[\p{Letter}\p{Mark}]+'}))
    last_name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':_("placeholder-surname"),'id':'last-name','pattern':'[\p{Letter}\p{Mark}]+'}))

    country_code = forms.CharField(max_length=5,required=True,widget=forms.TextInput(attrs={'placeholder':_("placeholder-countrycode"),'id':'countrycode','pattern':'^\+([0-9]{1,7})$'}))
    phone_number = forms.CharField(max_length=11,required=True,widget=forms.TextInput(attrs={'placeholder':'606 000 000','id':'phone-number','pattern':'^[0-9]+$'}))

    subject = forms.CharField(max_length=50,required=True,min_length=4,widget=forms.TextInput(attrs={'id':'subject'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':20,'id':'message'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __init__(self, *args, **kwargs):
        """ Adding classes for styling purposes. """
        super(SubmitContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'country_code':
                visible.field.widget.attrs['class'] = 'input-width-max form-control width-30 me-1'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

class DefaultPluginForm(forms.ModelForm):

    def clean(self):
        model = self.save(commit=False)

        language = self.instance.language

        show_link = self.cleaned_data.get('show_link', False)
        link_href = self.cleaned_data.get('link_href', None)
        link_title = self.cleaned_data.get('link_title', None)
        if show_link:
            # validate the activity name
            if link_href in EMPTY_VALUES:
                self._errors['link_href'] = self.error_class([
                    _("Link href can't be empty, when show_link is True.")])
            if link_title in EMPTY_VALUES:
                self._errors['link_title'] = self.error_class([
                    _("Link href can't be empty, when show_link is True.")])

        if link_href_taken(link_href,model,language):
            self._errors['link_href'] = self.error_class([
                _("Link href already taken.")])
        return self.cleaned_data

class WelcomeForm(DefaultPluginForm):
    class Meta:
        model = WelcomeModel
        exclude = ['link_manager']

class MainInfoForm(DefaultPluginForm):
    class Meta:
        model = MainInfoModel
        exclude = ['link_manager']

class ServiceListForm(DefaultPluginForm):
    class Meta:
        model = ServicesModel
        exclude = ['link_manager']


class ContactForm(DefaultPluginForm):
    class Meta:
        model = ContactFormModel
        exclude = ['link_manager']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        exclude = ['featured']

    def clean(self):
        model = self.save(commit=False)
        name = self.cleaned_data.get('name', None)
        language = self.instance.language
        if service_name_taken(name,model,language):
            self._errors['name'] = self.error_class([
                _("Name already taken.")])
        return self.cleaned_data