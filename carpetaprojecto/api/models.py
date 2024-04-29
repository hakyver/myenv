from django.db import models

# Create your models here.
class user(models.Model):
    titulo=models.CharField(max_length=50)
    fecha=models.DateField(auto_now_add=True, blank=True)
    descripcion=models.TextField(max_length=500)
    fuentes=models.URLField(max_length=500)

