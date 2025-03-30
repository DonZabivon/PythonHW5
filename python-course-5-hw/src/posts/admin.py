from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'likes_count']
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    
    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = "Likes"

admin.site.register(Post, PostAdmin)