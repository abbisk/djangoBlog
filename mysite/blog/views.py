from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Article
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def get_blogs(request):
    blogs=Blog.objects.all()
    response = 'Blogs:'
    for blog in blogs:
        response += '<br \> {0}'.format(blog)
        articles = Article.objects.filter(blog=blog)
        response += ','.join([article.title for article in articles])
    return HttpResponse(response)