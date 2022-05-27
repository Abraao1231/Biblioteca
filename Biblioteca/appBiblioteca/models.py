from django.db import models

class Book(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    data = models.DateField()

    def __str__(self):
        return self.nome

        