from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Мой сайт'
    text_1 = 'Главная страница'
    games = 'Магазин'
    cart = 'Корзина'
    home = 'Главная страница'

    context = {
        'title': title,
        'text_1': text_1,
        'games': games,
        'cart': cart,
        'home': home
    }
    return render(request, 'third_task/platform.html', context)

def games(request):
    title = 'Игры'
    game1 = 'Sims 4'
    game2 = 'Mount and Blade: Warband'
    game3 = 'Red Dead Redemption 2'
    sell = 'Купить'
    back = 'Вернуться обратно'

    context1={
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'sell': sell,
        'back': back
    }
    return render(request, 'third_task/games.html', context1)

def cart(request):
    title = 'Корзина'
    error = 'Извините, Ваша корзина пуста'
    back = 'Вернуться обратно'

    context2={
        'title': title,
        'error': error,
        'back': back

    }
    return render(request, 'third_task/cart.html', context2)