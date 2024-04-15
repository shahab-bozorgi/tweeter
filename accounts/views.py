from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from accounts.forms import UserEditForm
from home.models import Post


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # set user-specific data in the session
            request.session['username'] = username

            request.session.save()
            return redirect('/tweeter')
        else:
          pass

    else:
        # display the login form
        return render(request, 'accounts/login.html', {})


def user_register(request):
    context = {'Errors':[]}
    # if request.user.is_authenticated == True:
    #     return redirect('home_app:main')



    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context['Errors'].append("Passwords are not the same")
            return render(request, 'accounts/register.html', context)

        user = User.objects.create(username=username, password=password1)
        login(request, user)
        return redirect('home:tweets')
    return render(request, 'accounts/register.html')



def user_logout(request):
    logout(request)
    return redirect('/')



def user_profile(request, username):
    user = User.objects.get(username=username)
    tweet = Post.objects.filter(user=user.id).order_by('-id')

    return render(request, 'accounts/profile.html', {'tweet':tweet, 'user': user})


def user_edit(request):
    form = UserEditForm(instance=request.user)
    if request.method == 'POST':
        form = UserEditForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/edit_profile.html', {'form': form})