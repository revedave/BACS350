from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=200)

def __str__(self):
        return f'{self.name} by {self.identity}'
