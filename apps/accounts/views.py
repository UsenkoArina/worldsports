from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserLoginForm, UserRegistrationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from articles.models import Article, Comment

def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('articles:home')
            else:
                messages.error(request, "There was an error, try again...")
                return redirect('accounts:signin')
    else:
        form = UserLoginForm()
    return render(request, 'authentication/signin.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Creation
            User = get_user_model()
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                messages.success(request, f'Account created for {username}!')
            except IntegrityError:
                messages.error(request, 'This username or email already exists.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/registration.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('articles::home') 

@login_required
def profile_info(request):
    user = request.user
    last_login = user.last_login
    return render(request, 'authentication/profileInfo.html', {'form': None, 'username': user.username, 'registration_date': user.date_joined, 'last_login': last_login})

@login_required
def saved_articles(request):
    saved_articles = request.user.saved_articles.all().order_by('-pub_date')
    return render(request, 'authentication/saved_articles.html', {'saved_articles': saved_articles})

@login_required
def favorites_articles(request):
    favorite_articles = request.user.article_likes.all().order_by('-pub_date')
    return render(request, 'authentication/favorites.html', {'favorite_articles': favorite_articles})

@login_required
def commented_articles(request):
    commented_articles_ids = Comment.objects.filter(user=request.user).values_list('article', flat=True).distinct()
    commented_articles = Article.objects.filter(id__in=commented_articles_ids).order_by('-pub_date')
    return render(request, 'authentication/commented_articles.html', {'commented_articles': commented_articles})
