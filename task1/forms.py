from django import forms
# from django


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Ваше имя')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль')
    age = forms.CharField(max_length=3, label='Возраст')