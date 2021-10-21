from django.db import models
from django.urls.base import reverse_lazy

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.CharField()
    strength = models.CharField(max_length= 200, editable= True)
    weakness = models.CharField(max_length=200, editable= True)
    hero = models.CharField(max_length=200, editable=True)  

    def __str__(self):
        return f'{self.name} {self.identity} {self.description} {self.strength} {self.weakness}'

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])
