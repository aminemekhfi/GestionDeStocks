from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="Email utilisateur ", widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Prénom utilisateur ", max_length=70, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Nom utilisateur ", max_length=70, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label="Mot de passe",
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'})
    )
    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez votre mot de passe'})
    )
    username = forms.CharField(label="Nom de login de l'utilisteur ", max_length=70, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_staff = forms.BooleanField(label="Statut utilisateur (check si l'utilisteur pour modifier dans l'espace admin)", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    is_superuser = forms.BooleanField(label="Statut utilisateur (check si l'utilisteure et un admin)", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
