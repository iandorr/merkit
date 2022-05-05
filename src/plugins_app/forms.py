from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from plugins_app.models import ServiceModel

class SubmitContactForm(forms.Form):

    email = forms.EmailField(max_length=50,min_length=8,required=True,widget=forms.EmailInput(attrs={'placeholder':'me@domena.cz','id':'mail'}))
    first_name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Jan','id':'first-name','pattern':'[\p{Letter}\p{Mark}]+'}))
    last_name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Novák','id':'last-name','pattern':'[\p{Letter}\p{Mark}]+'}))

    country_code = forms.CharField(max_length=5,required=True,widget=forms.TextInput(attrs={'placeholder':'+420','id':'countrycode','pattern':'^\+([0-9]{1,7})$'}))
    phone_number = forms.CharField(max_length=9,required=True,widget=forms.TextInput(attrs={'placeholder':'606 000 000','id':'phone-number','pattern':'^[0-9]+$'}))

    subject = forms.CharField(max_length=50,required=True,min_length=4,widget=forms.TextInput(attrs={'id':'subject'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':20,'id':'message'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __init__(self, *args, **kwargs):
        super(SubmitContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'country_code':
                visible.field.widget.attrs['class'] = 'input-width-max form-control width-30 me-1'
            else:
                visible.field.widget.attrs['class'] = 'form-control'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        exclude = ['featured']