from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/socket-server/<str:room>/', consumers.ChatConsumer.as_asgi())
    re_path(r'ws/socket-server/(?P<room>\w+)/$', consumers.ChatConsumer.as_asgi())
]