from django.contrib.auth import get_user_model
from django.db import models

from MyBlog.articles.models import Article

UserModel = get_user_model()


class InfoAboutApp(models.Model):
    MAX_LEN_TITLE = 40

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        null=False,
        blank=False,
    )
    body = models.TextField(
        null=True,
        blank=True,
    )
