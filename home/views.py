from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, redirect
from home.models import Post, Comment
from accounts.models import Profile
from django.core.paginator import Paginator



def tweets(request):

    tweet = Post.objects.all().order_by('-id')
    page_number = request.GET.get('page')
    paginator = Paginator(tweet, 8)
    object_list = paginator.get_page(page_number)


    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        username = request.session['username']
        # profile = Profile.objects.get('image')
        author = User.objects.get(username=username)

        description = request.POST.get('description')
        Post.objects.create(description=description, user_id=author.id)

    return render(request, 'home/tweeter.html', {'tweet': object_list})

def comments(request, id):
    tweet = Post.objects.get(id=id)
    comments = Comment.objects.all()


    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        username = request.session['username']
        author = User.objects.get(username=username)
        tweet = request.POST.get('tweet')

        Comment.objects.create(tweet=tweet, parent_id=parent_id, user_id=author.id)

    return render(request, 'home/reply.html', {"comments": comments, 'tweet':tweet})

