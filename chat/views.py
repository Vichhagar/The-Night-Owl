from django.shortcuts import render
from ChatRoom.models import Room

def home(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, "chat/home.html", {"room":room})