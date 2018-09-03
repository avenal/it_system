from django import forms
from main.models import ContactModel
from django.core import validators

class ContactForm(forms.ModelForm):
    botcatcher = forms.CharField(required = False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'text')
