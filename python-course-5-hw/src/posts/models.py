from django.db import models
from users.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    likes = models.ManyToManyField(
        CustomUser, 
        related_name='liked_posts',
        blank=True
    )

    def __str__(self):
        return self.title