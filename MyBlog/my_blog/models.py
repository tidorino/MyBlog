from django.contrib.auth import get_user_model
from django.db import models

from MyBlog.articles.models import Article

UserModel = get_user_model()


# class PostLike(models.Model):
#     post = models.ForeignKey(
#         Article,
#         on_delete=models.RESTRICT,
#         null=False,
#         blank=True,
#     )
#     user = models.ForeignKey(
#         UserModel,
#         on_delete=models.RESTRICT,
#     )



# class InfoAboutApp(models.Model):
#     MAX_LEN_APP_NAME = 40
#
#     app_name = models.CharField(
#         max_length=MAX_LEN_APP_NAME,
#         null=False,
#         blank=False,
#     )
#     user = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE,
#     )
