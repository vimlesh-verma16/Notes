from django import forms 
from django.core import validators

def check_for_z(value):

    if value[0].lower() != 'z':
        raise forms.ValidationError("the name Needs start with z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
   
    email = forms.EmailField()
    verify_email = forms.EmailField(label= "Enter your mail again to verify")
    text = forms.CharField(widget = forms.Textarea)
    detail = forms.CharField(widget = forms.Textarea)


    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        vmail = all_cleaned_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("mismatch between the emails")

    

