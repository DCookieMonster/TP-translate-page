__author__ = 'dor'

from django import forms
from .models import User


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )


class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields =['username','password','email','first_name','last_name']
            # '__all__' # Or a list of the fields that you want to include in your form