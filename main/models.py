from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
class Cliente(models.Model):
  customer_name = models.CharField(max_length=64)
  customer_email = models.EmailField(max_length=40)
  message = models.TextField(null=False)

class Flan(models.Model):
  uuid = models.UUIDField(editable=False, default=uuid.uuid4)
  nombre = models.CharField(max_length=64)
  descripcion = models.TextField()
  precio = models.IntegerField()
  imagen_url = models.URLField()
  is_private =  models.BooleanField(default=False)

  def __str__(self) -> str:
    return self.nombre
  


