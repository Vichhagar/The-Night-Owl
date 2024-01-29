from django.urls import path
from . import views

app_name = "chatroom"
urlpatterns = [
    path('', views.home, name="home"),
    path('room/<slug>/', views.room, name="room"),
    path('create_room/', views.create_room, name="create_room"),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),

    path('user/<id>', views.userDashboard, name='user_dashboard'),
]