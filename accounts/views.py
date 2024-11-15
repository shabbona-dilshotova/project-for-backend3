from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect('news_list')
            else:
                return HttpResponse('Login Failed')
        else:
            return HttpResponse('Invalid form')
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'registration/login.html', context)
    

def user_logout(request):
    logout(request)
    return redirect('news_list')


def dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'user_profile.html', context)
