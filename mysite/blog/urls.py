from django.urls import path,include
from . import views

app_name='blog'

urlpatterns=[
    path('index/', views.index, name= 'index'),
    path('get_blogs/', views.get_blogs, name='get blogs'),
    path('get_counts/', views.get_counts, name='get countsd'),
]