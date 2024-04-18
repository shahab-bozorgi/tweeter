from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('register', views.user_register, name='register'),
    path("logout", views.user_logout, name="logout"),
    path('account/<str:username>', views.user_profile, name='profile'),
    path("editt", views.user_edit, name="edit"),

]