from django.db import models
from users.models import CustomUser
from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='replies'
    )
    
    # Лайки аналогично постам
    likes = models.ManyToManyField(
        CustomUser, 
        related_name='liked_comments',
        blank=True
    )

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"