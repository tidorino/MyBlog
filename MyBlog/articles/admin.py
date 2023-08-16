from django.contrib import admin

from MyBlog.accounts.models import BlogUser
from MyBlog.articles.models import Article, ArticleLike, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # ordering = ('title',)
    list_display = ('id', 'title','category', 'slug', 'status', 'author', 'created_on')
    list_filter = ('status',)
    search_fields = ('title',)
    sortable_by = ('created_on', 'author',)


@admin.register(ArticleLike)
class ArticleLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user')


