from django.contrib import admin

from MyBlog.accounts.models import BlogUser
from MyBlog.articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # ordering = ('title',)
    list_display = ('id', 'title', 'slug', 'status', 'author', 'created_on')
    list_filter = ('status',)
    search_fields = ('title',)
    sortable_by = ('created_on', 'author',)



