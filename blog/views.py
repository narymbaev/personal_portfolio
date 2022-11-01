from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blogs(request):
    blogs = Blog.objects.order_by('-date')[:3]
    context = {"blogs": blogs}
    # context = {}
    return render(request, 'blog/blogs.html', context)

def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {"blog": blog}
    return render(request, "blog/detail.html", context)