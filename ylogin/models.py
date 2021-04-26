from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=20)

    def __str__(self):
        print(self.username)