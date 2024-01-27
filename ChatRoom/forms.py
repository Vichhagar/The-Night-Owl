from django import forms
from .models import User, Room
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username", 
            "first_name", 
            "last_name", 
            "password1", 
            "password2", 
            "userBio", 
            "profileImage"
        ]

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username", 
            "first_name", 
            "last_name",
            "userBio",
            "profileImage"
        ]

class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "name",
            "room_type"
        ]