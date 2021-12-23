from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book, LibUser, RentBook
from .serializers import BookSerializer, LibUserSerializer, RentBookSerializer

# viewset :list, create, retrieve, update, partial_update, destroy




class BooksViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


# class BooksViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class LibuserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer

class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer
