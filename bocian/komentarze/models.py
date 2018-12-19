from django.db import models

# Create your models here.
from blog.models import Wpis


class Komentarz(models.Model):
    nick = models.CharField(max_length=15)
    email = models.CharField(max_length=25, blank=True, null=True)
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    wpis = models.ForeignKey(Wpis, on_delete=models.CASCADE)
    def __str__(self):
        return self.tytul
    class Meta:
        verbose_name_plural = "komentarze"
        ordering = ['data']

