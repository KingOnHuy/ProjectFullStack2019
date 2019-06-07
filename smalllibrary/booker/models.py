from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Binding(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    ISBN_10 = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    binding = models.ForeignKey(Binding,on_delete=models.SET_NULL, null=True)
    year = models.PositiveIntegerField()
    publisher = models.ForeignKey(Publisher,on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Borrow(models.Model):
    borrower = models.ForeignKey(User,on_delete=models.PROTECT)
    book = models.ForeignKey(Book,on_delete=models.PROTECT)

class Transaction(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    actor = models.ForeignKey(User,on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

# https://prod.liveshare.vsengsaas.visualstudio.com/join?B4CF6BB49D5786776FFEB74A9FF024073C85s
