from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hompepage, name=""),
    path('register', views.registration, name="register"),
    path('user-login', views.user_login, name="user-login"),
    path('dashboard', views.Dashboard, name="dashboard"),
]