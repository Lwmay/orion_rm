from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm

from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print(user.__dict__)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "registration/login.html", context)


def register_view(request):
    return render(request, "registration/register.html")


def user_create_user(*args, **kwargs):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.save()


def logout_view(request):
    logout(request)
    return redirect('/users/login')
