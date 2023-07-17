from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index_page(request):
    
    if request.user.is_authenticated:
        try:
            get_avatar = MyUserAvatar.objects.get(user=request.user)
            return render(request, "to_do/index.html", context={
            "avatar":get_avatar
            })
        except ObjectDoesNotExist:
            return render(request, "to_do/index.html")
    else:
        return render(request, "to_do/index.html")


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'to_do/signup.html', context={'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homepage')
            except IntegrityError:
                form = UserCreationForm()
                return render(request, 'to_do/signup.html', context={'form':form,
                'error':'Этот пользователь уже зарегистрирован!'})
        else:
            form = UserCreationForm()
            return render(request, 'to_do/signup.html', context={'form':form,
            'error':'Пароли не совпадают!'})


def signin_user(request):
    if request.method == "GET":
        return render(request, 'to_do/signin.html', context={
            "form": AuthenticationForm(),
        })
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST['password'])
        if user is None:
            return render(request, 'to_do/signin.html', context={
            "form": AuthenticationForm(),
            "error": "Пользователь не найден!"
        })
        else:
            login(request, user)
            return redirect("homepage")
