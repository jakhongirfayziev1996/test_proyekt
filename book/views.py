from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets

from .models import Book, LibUser, RentBook
from .serializers import BookSerializer, LibUserSerializer, RentBookSerializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LibuserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer

class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer
