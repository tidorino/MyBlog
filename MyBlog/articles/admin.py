from django.contrib import admin

from MyBlog.accounts.models import BlogUser
from MyBlog.articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_on')


