from django.db import models

class Albhum(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    releades_year = models.IntegerField()

    def __str__(self):
        return self.name
class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    albhum = models.ForeignKey(Albhum, on_delete=models.CASCADE)

    def __str__(self):
        return self.title