from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .forms import *

# Create your views here.

def index_page(request):
    form = PostForm()
    if request.user.is_authenticated:
        try:
            works = ToDo.objects.filter(user=request.user).order_by("-create_date")
            get_avatar = MyUserAvatar.objects.get(user=request.user)
            return render(request, "to_do/index.html", context={
            "avatar":get_avatar,
            "form":form,
            "works":works
            })
        except ObjectDoesNotExist:
            return render(request, "to_do/index.html", context={
                'form':form
            })
    else:
        return render(request, "to_do/index.html", context={
            'form': form
        })


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'to_do/signup.html', context={'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                icon = MyUserAvatar.objects.create(user=user)
                icon.save()
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


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect(to="homepage")


def to_do_maker(request):
    if request.method == "POST":
        user_form = PostForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_to_do = user_form.save(commit=False)
            new_to_do.user = request.user
            new_to_do.save()
            return redirect(to="homepage")
