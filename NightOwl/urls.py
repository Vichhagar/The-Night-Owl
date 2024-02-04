from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ChatRoom.urls")),
    path('room/<slug>/', include("chat.urls")),
]
