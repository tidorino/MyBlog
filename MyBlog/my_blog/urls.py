from django.urls import path

from MyBlog.my_blog.views import index

urlpatterns = (
    path('', index, name='index'),
  )
