from django.contrib.auth import get_user_model
from django.shortcuts import render

from MyBlog.articles.models import Article


UserModel = get_user_model()


def index(request):
    posts = Article.objects.all()
    blog_user = UserModel.objects.all()

    context = {
        'posts': posts,
        'blog_user': blog_user,
    }

    return render(request, 'my_blog/home-page.html', context)


