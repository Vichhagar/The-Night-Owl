from django.shortcuts import render
from .models import User, Room, Text

def home(request):
    rooms = Room.objects.all()
    return render(request, "ChatRoom/home.html", {"rooms": rooms})

def room(request, slug):
    print(slug)
    return render(request, "ChatRoom/room.html", {"slug":slug})