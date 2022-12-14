from django import forms
from django.contrib.auth import get_user_model

from MyBlog.accounts.models import Profile
from MyBlog.articles.models import Article

UserModel = get_user_model()


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = '__all__'
        # fields = ('author', 'category', 'title', 'slug', 'body', 'image_url')
        labels = {
            'image_url': 'Article image',
        }
