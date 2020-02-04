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

def add_blog(request, blog_id=None):
    if blog_id:
        blog = Blog.objects.get(id=blog_id)
    else:
        blog=Blog()

    if request.method == 'POST':
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return get_blogs(request)
        else:
            context = {'form': form}
            return render(
                request,'add_blog.html', context)
    blog_form = BlogForm(instance=blog)
    context = {'form': blog_form, 'blog': blog}
    return render(request, 'add_blog.html', context)
            