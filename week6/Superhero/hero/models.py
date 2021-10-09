from django.db import models
from django.urls.base import reverse_lazy

class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    strength = models.CharField(max_length= 200)
    weakness = models.CharField(max_length=200)
    hero = models.CharField(max_length=200, default="00000", editable=True)  

    def __str__(self):
        return f'{self.name} {self.identity} {self.description}'

    def get_absolute_url(self):
        return reverse_lazy('book_detail', args=[str(self.id)])
