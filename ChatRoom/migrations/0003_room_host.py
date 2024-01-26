# Generated by Django 4.1.1 on 2024-01-26 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChatRoom', '0002_room_name_room_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
