from rest_framework import serializers
from .models import MessageFront


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageFront
        fields = ('user', 'date', 'screen', 'event')