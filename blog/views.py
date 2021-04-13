from django.shortcuts import render
from .models import Blog
# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'all_blogs.html', {"blogs": blogs})