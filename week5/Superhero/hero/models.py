from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    hero = models.CharField(max_length=200, default="00000", editable=True)  

    def __str__(self):
        return f'{self.name} {self.identity} {self.description}'

