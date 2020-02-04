from blog.models import Blog,Article
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'draft']