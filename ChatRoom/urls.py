from django.urls import path
from . import views

app_name = "chatroom"
urlpatterns = [
    path('', views.home, name="home"),
    path('<slug>', views.room, name="room")
]