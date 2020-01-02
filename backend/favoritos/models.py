from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favoritos(models.Model):
    imdbID = models.CharField(max_length=20)
    user_id = models.ForeignKey(
        User, related_name="id", on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)