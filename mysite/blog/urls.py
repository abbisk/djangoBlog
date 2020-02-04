from django.urls import path,include
from . import views

app_name='blog'

urlpatterns=[
    path('index/', views.index, name= 'index'),
    path('get_blogs/', views.get_blogs, name='get blogs'),
    path('add_blog/', views.add_blog, name = 'add blog'),
    path('add_blog/<int:blog_id>/', views.add_blog, name='edit_blog'),
] 