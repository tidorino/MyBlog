from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

from MyBlog.accounts.models import Profile
from MyBlog.articles.models import Article


UserModel = get_user_model()

"""
{% if user.id == post.author.id %}
***
<div class="container">
<h1>Post</h1>
{% for post in object_list %}
{% empty %}
    <h1>You have not written any posts yet!</h1>
{% if user.is_authenticated %}
{% if user.id == post.author.id %}
    <li><a href="{% url 'app1:article-detail' post.pk %}">{{post.title}}</a> -
    {{post.author}} - <small>{{post.post_date}}</small> - <small> category : <a href="{% url 'app1:category' post.category|slugify %}">{{post.category}}</a> - </small>
    <small><a href="{% url 'app1:updatepost' post.pk %}">Edit</a></small><small>
    <a href="{% url 'app1:deletepost' post.pk %}">- Delete</a>  
    </small></li>
    {{post.snippet}}
    {% endif %}
    {% endif %}
{% endfor %}
</div>
"""


def index(request):
    user = UserModel.objects.all()
    posts = Article.objects.all()
    profile = Profile.objects.all()

    context = {
        'posts': posts,
        'user': user,
        'profile': profile,
        'no_profile': True,
    }

    return render(request, 'my_blog/home-page.html', context)


# class IndexViewWithTemplate(TemplateView, PermissionRequiredMixin):
#     template_name = 'my_blog/home-page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # Add specific view stuff, one or more
#         context['users'] = UserModel.objects.all()
#         context['posts'] = Article.objects.all()
#         # context['form'] = MyForm()
#
#         # Return the ready-to-use context
#         return context
