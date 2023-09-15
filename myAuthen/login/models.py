from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title
    
