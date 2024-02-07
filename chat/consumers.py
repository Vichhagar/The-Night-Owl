import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from ChatRoom.models import User, Room, Text

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room']
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()



    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['data']

        print(f"message in the group:: {message}")
        # saving message into the database
        text_to_save = Text()

        text_to_save.text_body = message
        text_to_save.text_sender = self.scope["user"]

        room_id = self.scope['url_route']['kwargs']['room']

        if room_id:
            room_instance = Room.objects.get(id=room_id)
            text_to_save.text_room = room_instance
            text_to_save.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )

    def chat_message(self, event):
        message = event['message']
        print("MESSAGE:: ", message)
        sender = User.objects.get(id=message[1])

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message[0],
            'sender_name':sender.username
        }))