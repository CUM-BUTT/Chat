from django.db import models

class User(models.Model):
    name = models.CharField('name', max_length=20, primary_key=True, )
    password = models.CharField('password', max_length=100, )