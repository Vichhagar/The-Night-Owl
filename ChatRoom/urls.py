from django.urls import path
from . import views

app_name = "chatroom"
urlpatterns = [
    path('', views.home, name="home"),
    path('<slug>', views.room, name="room"),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
]