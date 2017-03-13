# -*- coding: UTF-8 -*-


from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    def __str__(self):
        return '%s. %s. %s' % (self.name, self.author, self.pub_date)
