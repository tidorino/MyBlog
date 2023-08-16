from django.contrib import admin

from MyBlog.my_blog.models import InfoAboutApp


# from MyBlog.my_blog.models import PostLike


@admin.register(InfoAboutApp)
class InfoAboutAppAdmin(admin.ModelAdmin):

    list_display = ('title', 'body')


