from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Borrow(models.Model):
    borrower = models.ForeignKey(User,on_delete=models.PROTECT)
    book = models.ForeignKey(Book,on_delete=models.PROTECT)

class Book(models.Model):
    title = models.CharField(max_length=255)
    ISBN_10 = models.CharField(max_length=255)
    author = models.CharField(map_length=255)
    binding = models.ForeignKey(Borrow,on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallInteger()
    publisher = models.ForeignKey(Publisher,on_delete=models.SET_NULL, null=True)

class Publisher(models.Model):
    name = models.CharField(max_length=255)

class Binding(models.Model):
    name = models.CharField(max_length=255)

class Transaction(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    actor = models.ForeignKey(User,on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
