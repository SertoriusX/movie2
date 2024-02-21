from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    email = forms.EmailField(max_length=50,required=True)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=30,required=True)
    email=forms.EmailField(max_length=50,required=True)
    message=forms.TimeField(required=True,widget=forms.Textarea)
    class Meta:
        model=Contact
        fields=['name','email','message']