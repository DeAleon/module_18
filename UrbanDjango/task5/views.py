from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

users = ['Alex', 'Max', 'Ugrozina']

def sign_up_by_html(request):
    info = {
        'form': UserRegister(),
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if name in users:
                info['error']='Пользователь уже существует'

            elif password != repeat_password:
                info['error']='Пароли не совпадают'

            elif int(age) < 18:
                info['error']='Вы должны быть старше 18'

            else:
                return HttpResponse(f'Приветствуем, {name}!')

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if name in users:
            info['error']='Пользователь уже существует'

        elif password != repeat_password:
            info['error']='Пароли не совпадают'

        elif int(age) < 18:
            info['error']='Вы должны быть старше 18'

        else:
            return HttpResponse(f'Приветствуем, {name}!')

    return render(request, 'fifth_task/registration_page.html', info)