from django.shortcuts import render
from .models import Value, Principle
from .serializers import ValuesSerializer, PrinciplesSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Datas to be passed on.
class ValuesViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permissions_classes = (IsAuthenticated,)
    queryset = Value.objects.all()
    serializer_class = ValuesSerializer

class PrinciplesViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permissions_classes = (IsAuthenticated,)
    queryset = Principle.objects.all()
    serializer_class = PrinciplesSerializer

