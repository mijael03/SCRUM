from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home') 
        
class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.CharField(max_length=255, default='coding')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')

class Comentario(models.Model):
    comentario = models.TextField(blank= False, null= False)
    fecha_comentario = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)