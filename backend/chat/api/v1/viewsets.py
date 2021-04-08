from rest_framework import authentication
from chat.models import Thread, ThreadAction, ThreadMember
from .serializers import (
    ThreadSerializer,
    ThreadActionSerializer,
    ThreadMemberSerializer,
)
from rest_framework import viewsets


class ThreadViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Thread.objects.all()


class ThreadMemberViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadMemberSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ThreadMember.objects.all()


class ThreadActionViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadActionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ThreadAction.objects.all()
