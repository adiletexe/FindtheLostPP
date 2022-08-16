from django.shortcuts import render, redirect
from .models import Categories, FoundItems
from .forms import CreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Home Page
def index(request):
    # category = request.GET.get('category')
    # if category == None:
    founditems = FoundItems.objects.all()
    # else:
    #     founditems = FoundItems.objects.filter(category__name__contains = category)
    #
    return render(request, 'lostandfoundapp/index.html', {'founditems':founditems})

# Adding lost item
@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'lostandfoundapp/create.html', {'form': CreationForm})
    else:
        try:
            form = CreationForm(request.POST)
            form.save()
            return redirect('index')
        except:
            return render(request, 'lostandfoundapp/create.html', {'form': CreationForm, 'error':'Don\'t do experiments please'})

def signupsystem(request):
    if request.method == "GET":
        return render(request, 'lostandfoundapp/signupsystem.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'lostandfoundapp/signupsystem.html', {'form': UserCreationForm, 'error':'passwords doesn\'t match!'})
        else:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'lostandfoundapp/signupsystem.html',
                              {'form': UserCreationForm, 'error': 'Username is already taken!'})

def loginsystem(request):
    if request.method == "GET":
        return render(request, 'lostandfoundapp/loginsystem.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'lostandfoundapp/loginsystem.html', {'form': AuthenticationForm, 'error':'Username and password doesn\'t match'})

@login_required
def logoutsystem(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')