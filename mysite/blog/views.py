from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Article
from blog.forms import BlogForm, ArticleForm
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def get_blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Blog created")
        else:
            context = {'form': form}
            return render(
                request,'add_blog.html', context)
    context = {'form': BlogForm()}
    return render(request, 'add_blog.html', context)
            