from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Favoritos(models.Model):
    imdbID = models.CharField(max_length=20) #id do filme vindo da API OMDB
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
