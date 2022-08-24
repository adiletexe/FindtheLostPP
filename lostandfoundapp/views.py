from django.shortcuts import render, redirect, get_object_or_404
from .models import Categories, FoundItems
from .forms import CreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Home Page
def index(request):
    oldest = request.GET.get('oldest')
    categories = Categories.objects.all()
    category = request.GET.get('category')
    if category is not None:
            founditems = FoundItems.objects.filter(category__name__contains = category).order_by('-date')
    else:
        founditems = FoundItems.objects.all().order_by('-date')
    return render(request, 'lostandfoundapp/index.html', {'founditems':founditems, 'categories':categories})

def oldest(request):
    oldest = request.GET.get('oldest')
    categories = Categories.objects.all()
    category = request.GET.get('category')
    if category is not None:
        founditems = FoundItems.objects.filter(category__name__contains=category).order_by('date')
    else:
        founditems = FoundItems.objects.all().order_by('date')
    return render(request, 'lostandfoundapp/oldest.html', {'founditems': founditems, 'categories': categories})


# auth
def signupsystem(request):
    if request.method == "GET":
        return render(request, 'lostandfoundapp/signupsystem.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'lostandfoundapp/signupsystem.html',
                          {'form': UserCreationForm, 'error': 'Passwords don\'t match!'})
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
            return render(request, 'lostandfoundapp/loginsystem.html',
                          {'form': AuthenticationForm, 'error': 'Username and password doesn\'t match!'})


@login_required
def logoutsystem(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')


# Adding lost item
@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'lostandfoundapp/create.html', {'form': CreationForm()})
    else:
        form = CreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                newitem = form.save(commit=False)
                newitem.user = request.user
                form.save()
                return redirect('index')
            except ValueError:
                return render(request, 'lostandfoundapp/create.html', {'form': CreationForm(), 'error':'Don\'t do experiments please'})
        else:
            return render(request, 'lostandfoundapp/create.html', {'form': CreationForm(), 'error':'Don\'t do experiments please'})

def viewpost(request, post_pk):
    post = get_object_or_404(FoundItems, pk=post_pk)
    return render(request, 'lostandfoundapp/viewpost.html', {'post':post})

@login_required
def myposts(request):
    categories = Categories.objects.all()
    category = request.GET.get('category')
    if category is not None:
        myposts = FoundItems.objects.filter(category__name__contains=category, user=request.user).order_by('-date')
    else:
        myposts = FoundItems.objects.filter(user=request.user).order_by('-date')

    return render(request, 'lostandfoundapp/myposts.html', {'myposts': myposts, 'categories': categories})

def delete(request, post_pk):
    post = get_object_or_404(FoundItems, pk=post_pk, user=request.user)
    if request.method == "POST":
        post.delete()
        return redirect('index')

