from django.shortcuts import render


def index(request):
    title = 'Главная страница'
    games = 'Магазин'
    carts = 'Корзина'
    home = 'Главная страница'

    context = {
        'title': title,
        'games': games,
        'carts': carts,
        'home': home,
    }
    return render(request, 'fourth_task/menu.html', context)

def games(request):
    title = 'Игры'
    game = ['Sims 4', 'Mount and Blade: Warband', 'Red Dead Redemption 2']
    sell = 'Купить'
    games = 'Магазин'
    carts = 'Корзина'
    home = 'Главная страница'

    context1={
        'title': title,
        'game': game,
        'sell': sell,
        'games': games,
        'carts': carts,
        'home': home,
    }
    return render(request, 'fourth_task/games.html', context1)

def cart(request):
    title = 'Корзина'
    error = 'Извините, Ваша корзина пуста'
    games = 'Магазин'
    carts = 'Корзина'
    home = 'Главная страница'

    context2={
        'title': title,
        'error': error,
        'games': games,
        'carts': carts,
        'home': home,
    }
    return render(request, 'fourth_task/cart.html', context2)