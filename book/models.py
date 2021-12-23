from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to="rasmlar", null=True, blank=True)
    kg = models.IntegerField()

class LibUser(models.Model):
    jerjero = models.CharField(max_length=100)
    fakaferi = models.IntegerField(null=True, blank=True)

class RentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    rentDate = models.DateTimeField(auto_now_add=True)
    reterneddate = models.DateTimeField(null=True, blank=True)



