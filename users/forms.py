from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Имя пользователя'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Пароль'})
    )

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Имя пользователя'}),
    )
    email = forms.CharField(
        max_length=150,
        widget=forms.EmailInput(attrs={'class': 'form-control ', 'placeholder':'Электронная почта'}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder':'Пароль'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder':'Подтвердите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 
 
