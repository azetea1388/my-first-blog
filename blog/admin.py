from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "published_date", "author"]
    search_fields = ["title", "content"]
    list_filter = ["published_date"]
    class Meta:
        model = Post
        
admin.site.register(Post)