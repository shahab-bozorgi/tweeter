from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User



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
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context['Errors'].append("Passwords are not the same")
            return render(request, 'accounts/register.html', context)

        user = User.objects.create(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home:tweets')
    return render(request, 'accounts/register.html')


