from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','created_at','author','is_published')
    list_display_links=('title',)
    list_filter=('created_at','author','is_published')
    
    

admin.site.register(Post,PostAdmin)