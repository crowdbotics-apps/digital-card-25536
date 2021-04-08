from rest_framework import serializers
from chat.models import Thread, ThreadAction, ThreadMember


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = "__all__"


class ThreadMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadMember
        fields = "__all__"


class ThreadActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadAction
        fields = "__all__"
