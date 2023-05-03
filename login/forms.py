from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    Choices = [
        (0, 'Maintenance'), (1, 'User')
    ]
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=Choices)

    class Meta:
        model = User
        fields = ['type', 'username', 'email', 'password1', 'password2']
