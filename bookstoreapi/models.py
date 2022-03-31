from django.db import models

class Book(models.Model):
    booktitle = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    coverPrice = models.CharField(max_length=10)

    def __str__ (self):
        return self.author + ' ' + self.booktitle