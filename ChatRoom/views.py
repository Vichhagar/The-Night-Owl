from django.shortcuts import render, redirect
from .models import User, Room, Text
from .forms import CreateUserForm, UpdateUserForm, CreateRoomForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('chatroom:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('chatroom:home')
            else:
                messages.info(request, "username or password is wrong")
                
        return render(request, 'ChatRoom/login.html')

@login_required(login_url='chatroom:login')
def logoutUser(request):
    logout(request)
    return redirect('chatroom:login')

def register(request):
    if request.user.is_authenticated:
        return redirect('chatroom:home')
    else:
        form = CreateUserForm()
        print(form)
        if request.method == "POST":
            form = CreateUserForm(request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "account created")
                return redirect('chatroom:login')

        context = {
            "form" : form
        }
        return render(request, 'ChatRoom/registration.html', context)

@login_required(login_url='chatroom:login')
def home(request):
    rooms = Room.objects.all()
    return render(request, "ChatRoom/home.html", {"rooms": rooms})

@login_required(login_url='chatroom:login')
def room(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, "ChatRoom/room.html", {"room":room})

@login_required(login_url='chatroom:login')
def userDashboard(request, id):
    user = User.objects.get(id=id)
    return render(request, "ChatRoom/user_dashboard.html", {"user": user})

def create_room(request):
    form = CreateRoomForm()
    print(form)
    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "room created")
            return redirect('chatroom:home')

    context = {
        "form" : form
    }
    return render(request, 'ChatRoom/create_room.html', context)