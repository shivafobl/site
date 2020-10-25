from django.shortcuts import render
from .models import Post
# Create your views here.
def blog_home(request):
    
    posts= Post.objects.all().filter(is_published=True).order_by('-created_at')
    
    context ={
        'posts':posts,
        }
    return render(request,'blog/blog.html',context)