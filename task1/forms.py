from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from django


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Ваше имя')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль')
    age = forms.CharField(max_length=3, label='Возраст')


class CustomLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(), max_length=30)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), min_length=8)