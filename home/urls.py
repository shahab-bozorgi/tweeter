from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('tweeter', views.tweets, name='tweets'),
    path('comment/<int:id>', views.comments, name='comments'),


]
