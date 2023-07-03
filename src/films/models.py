from django.db import models
import re

def poster_path(instance, filename):
    adj_title = instance.title
    adj_title = adj_title.lower()
    adj_title = re.sub(r'[^\w\s]', '', adj_title)
    adj_title = adj_title.replace(" ", "_")
    adj_ry = instance.release_year
    return f"posters/{adj_title + '_' + str(adj_ry)}/{filename}"

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    director = models.CharField(max_length=150)
    rating = models.FloatField()
    poster = models.ImageField(upload_to=poster_path, blank=True)

    def __str__(self):
        return f"{self.title} {self.release_year}"