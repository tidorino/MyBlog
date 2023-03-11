from django import forms
from django.contrib.auth import get_user_model

from MyBlog.articles.models import Article

UserModel = get_user_model()


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'post_image': 'Article image',
        }

    # def clean_author(self):
    #     author = self.cleaned_data.get('author')
    #     if not author:
    #         author = self.author.user
    #     return author
