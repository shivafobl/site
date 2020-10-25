from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    
    title=models.CharField(max_length=120)
    description=models.TextField()
    img = models.ImageField(upload_to='photos/')
    author=models.CharField(max_length=50)
    created_at=models.DateField(default=datetime.now,blank=True)
    is_published=models.BooleanField(default=False)
    
    
    
    def __str__(self):
            return self.title
        
    


        
    class Meta:
        
        verbose_name='post'
        verbose_name_plural='posts'
        
        
        