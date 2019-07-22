from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Tutorial
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.


def homepage(request):
    return render(request=request, template_name='main/home.html', context={'tutorials': Tutorial.objects.all})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request=request,template_name='main/register.html', context={'form': form})

    form = NewUserForm()
    return render(request=request,template_name='main/register.html', context={'form': form})


def logout_request(request):
    logout(request)
    messages.info(request,'You Are Successfully Logged Out')
    return redirect('main:homepage')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"form": form})


def about_us(request):
    return render(request=request, template_name='main/about_us.html', context={})


def contact_us(request):
    return render(request=request, template_name='main/contact_us.html', context={})


def services(request):
    return render(request=request, template_name='main/services.html', context={})


# def legaldocsformats(request):
#     return render(request=request, template_name='main/ldformats.html', context={})
