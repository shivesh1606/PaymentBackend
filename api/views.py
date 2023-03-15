from rest_framework import viewsets
from .models import Transaction, ExtendedUser
from .serializer import TranscationSerializer, ExtendedUserSerializer


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TranscationSerializer


class ExtendedUserView(viewsets.ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializer
