# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=30,
                               help_text="Le nom d'utilisateur contient 30 \
                               caractères maximum. \
                               Doit uniquement contenir \
                               des lettres ou les symboles @/./+/-/_",
                              )
    email = forms.EmailField(label="Adresse mail")

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("username", "password")

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=30,
                               help_text="Le nom d'utilisateur contient 30 \
                               caractères maximum. \
                               Doit uniquement contenir \
                               des lettres ou les symboles @/./+/-/_",
                              )
    email = forms.EmailField(label="Adresse mail")
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class CustomUserChangePassword(PasswordChangeForm):

    class Meta:
        model = CustomUser
