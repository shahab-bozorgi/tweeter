from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView

from home.models import Post, Comment
from accounts.models import Profile
from django.core.paginator import Paginator


def tweets(request):
    tweet = Post.objects.all().order_by('-id')
    page_number = request.GET.get('page')
    paginator = Paginator(tweet, 8)
    object_list = paginator.get_page(page_number)

    if request.method == 'POST':
        username = request.session['username']
        author = User.objects.get(username=username)
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Post.objects.create(description=description, user_id=author.id, image=image)
        return redirect('home:tweets')

    return render(request, 'home/tweeter.html', {'tweet': object_list})


def comments(request, id):
    tweet = Post.objects.get(id=id)
    comments = Comment.objects.all().order_by('-created')

    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        username = request.session['username']
        author = User.objects.get(username=username)
        reply = request.POST.get('reply')

        Comment.objects.create(tweet=reply, parent_id=parent_id, user_id=author.id)

    return render(request, 'home/reply.html', {"comments": comments, 'tweet': tweet, 'id': id})


# class PostView( DetailView):
#     model = Post
#     template_name = 'home/tweeter.html'
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     if self.request.user.likes.filter(user_id=self.request.user.id):
#         context["is_liked"] = True
#     else:
#         context["is_liked"] = False
#     return context

# def like(request, id, pk):
#     if request.user.is_authenticated:
#         try:
#             like = Like.objects.get(user_id=request.user.id)
#             like.delete()
#             return JsonResponse({'response': 'unliked'})
#
#
#         except:
#             Like.objects.create(post_id=pk, user_id=request.user.id)
#             return JsonResponse({'response': 'liked'})
#



