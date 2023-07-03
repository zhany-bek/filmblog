from django.contrib.auth.models import User
from django.db import models
from films.models import Film

def pfp_path(instance, filename):
    return f"pfps/{instance.user.username}/{filename}"

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    favorites = models.ManyToManyField(Film, related_name="profiles", blank=True)
    profile_picture = models.ImageField(upload_to=pfp_path, blank=True)

    def __str__(self):
        return f"{self.user.username}"