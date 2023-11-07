from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    name= models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.PositiveIntegerField(max_length=10)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.name