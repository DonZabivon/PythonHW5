from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at', 'likes_count']
    raw_id_fields = ['post', 'author']
    
    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = "Likes"

admin.site.register(Comment, CommentAdmin)