from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from django.shortcuts import render

from MyBlog.accounts.models import Profile
from MyBlog.articles.models import Article


UserModel = get_user_model()


def index(request):
    user = UserModel.objects.all()
    posts = Article.objects.all()
    profile = Profile.objects.all()
    paginator = Paginator(posts, 6)
    page = request.GET.get('page', 1)
    page_object = paginator.get_page(page)

    context = {
        'posts': posts,
        'user': user,
        'profile': profile,
        'no_profile': True,
        'page_object': page_object,
        # 'liked_posts': liked_posts,
    }

    return render(request, 'my_blog/home-page.html', context)



