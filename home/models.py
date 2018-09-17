from django.db import models


class User(models.Model):
    def __str__(self):
        return self.username

    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)


class Account(models.Model):

    def __str__(self):
        return str(self.username.username)

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

