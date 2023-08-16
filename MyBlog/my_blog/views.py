from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render

from MyBlog.accounts.models import Profile
from MyBlog.articles.models import Article
from MyBlog.my_blog.models import InfoAboutApp

UserModel = get_user_model()


def index(request):
    user = UserModel.objects.all()
    posts = Article.objects.filter(status=1).order_by('-created_on')
    profile = Profile.objects.all()
    paginator = Paginator(posts, 6)
    page = request.GET.get('page', 1)
    page_object = paginator.get_page(page)
    info_app = InfoAboutApp.objects.all()

    context = {
        'posts': posts,
        'user': user,
        'profile': profile,
        'no_profile': True,
        'page_object': page_object,
        'info_app': info_app,
        # 'liked_posts': liked_posts,
    }

    return render(request, 'my_blog/home-page.html', context)


# def category_view(request, category):
#     post = Article.objects.filter(category=category)
#     category_posts = ShowByCategory.objects.get(post=post)
#     print(category_posts)
#     context = {
#         'category': category_slug,
#         'category_posts': category_posts,
#     }
#     return render(request, 'my_blog/categories.html', context)




