from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    ttt = 'abcde'

    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register(request):
    if request.method != 'POST':
        print('not post')
        form = CustomUserForm()
    else:
        print('post')
        form = CustomUserForm(request.POST)
        if form.is_valid():
            print('form valid')
            form.save()
            return redirect(reverse('login'))
        else:
            print(form.errors)

    context = {'form': form, 'error': form.errors}

    return render(request, 'app_auth/register.html', context)

    # if request.method == "POST":
    #     form = CustomUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('users:login')
    #
    #     context = {'form': form}
    #     return render(request, 'users/register.html', context)
    # else:
    #     return (render(request, 'app_auth/register.html'))