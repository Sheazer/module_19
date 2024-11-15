from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


def sign_up_by_django(request):
    users = Buyer.objects.all()
    buyer = []
    for user in users:
        buyer.append(user.name)
        print(user.name)
    print(buyer)
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
            elif info['name'] in buyer:
                info['error'] = 'Такой пользователь существует!'
                return render(request, 'task1/registration_page.html', {'form': form, 'info': info})
            else:
                info['error'] = 'Success'
                Buyer.objects.create(name=info['name'], balance=1000, age=info['age'])
                return render(request, 'task1/registration_page.html', {'form': form, 'info': info, 'username': info['name']})
    else:
        form = UserRegister()
        info['error'] = 'Empty'
        print('Failed==============================>')
    return render(request, 'task1/registration_page.html', {'form': form, 'info': info})


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


