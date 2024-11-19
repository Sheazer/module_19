from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister, CustomLoginForm
from .models import *


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            info['name'] = form.cleaned_data['username']
            info['password'] = form.cleaned_data['password']
            info['repeat_password'] = form.cleaned_data['repeat_password']
            info['age'] = form.cleaned_data['age']
            if info['password'] != info['repeat_password']:
                info['error'] = 'Пароли не совпадают!'
                return render(request, 'task1/registration_page.html', {'form': form, 'info': info})
            elif int(info['age']) < 18:
                info['error'] = 'Вы должны быть старше 18!'
                return render(request, 'task1/registration_page.html', {'form': form, 'info': info})
            elif Buyer.objects.filter(name=info['name']).exists():
                info['error'] = 'Такой пользователь существует!'
                return render(request, 'task1/registration_page.html', {'form': form, 'info': info})
            else:
                info['error'] = 'Success'
                Buyer.objects.create(name=info['name'], balance=1000, age=info['age'], password=info['password'])
                return render(request, 'task1/registration_page.html',
                              {'form': form, 'info': info, 'username': info['name']})
    else:
        form = UserRegister()
        info['error'] = 'Empty'
        print('Failed==============================>')
    return render(request, 'task1/registration_page.html', {'form': form, 'info': info})


def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            try:
                # Ищем пользователя по имени
                user = Buyer.objects.get(name=form.cleaned_data['username'])
            except Buyer.DoesNotExist:
                # Если пользователь не найден
                return render(request, 'task1/login.html', {
                    'form': form,
                    'info': 'Такого пользователя нет!',
                    'check': False,
                })

            # Проверяем пароль
            if form.cleaned_data['password'] == user.password:
                return render(request, 'task1/login.html', {
                    'form': form,
                    'info': f'Добро пожаловать, {form.cleaned_data["username"]}!',
                    'check': True,
                })
            else:
                # Неверный пароль
                return render(request, 'task1/login.html', {
                    'form': form,
                    'info': 'Неверный пароль!',
                    'check': True,
                })
    else:
        form = CustomLoginForm()

    return render(request, 'task1/login.html', {'form': form, 'check': False})

def main_template(request):
    title = 'Учебный портал'
    head = 'Главная страница'
    main = 'Главная'
    courses = 'Курсы'
    profile = 'Мой профиль'
    context = {
        'title': title,
        'head': head,
        'main': main,
        'courses': courses,
        'profile': profile,
    }
    return render(request, 'task4/main.html', context)


def courses(request):
    title = 'Игры Ииу'
    head = 'Мои игры'
    games = Game.objects.all()
    home = 'Главная страница'
    context = {
        'title': title,
        'head': head,
        'courses': courses,
        'home': home,
        'games': games,
    }
    return render(request, 'task4/courses.html', context)


def profile(request):
    title = 'Мой профиль'
    head = 'Мои данные'
    user = Buyer.objects.get(id=8)
    name = user.name
    age = user.age
    balance = user.balance
    context = {
        'title': title,
        'head': head,
        'name': name,
        'age': age,
        'balance': balance,
        'home': 'Главная страница',
    }

    return render(request, 'task4/profile.html', context)
