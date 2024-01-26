from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE = [
        ('admin', 'admin'),
        ('official', 'official'),
        ('normal', 'normal')
    ]
    profileImage = models.ImageField(upload_to='images/', null=True, blank=True)
    userType = models.CharField(max_length=10, choices=USER_TYPE, default='normal')
    userBio = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Room(models.Model):
    ROOM_TYPE = [
        ('public', 'public'),
        ('private', 'private')
    ]
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length = 200)
    name = models.CharField(max_length=200)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE)

    def __str__(self):
        return self.slug


class Text(models.Model):
    date_created = models.DateTimeField()
    text_body = models.TextField()
    text_sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text_room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text_sender} said {self.text_body[:15]}"
