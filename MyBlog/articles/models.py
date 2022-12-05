from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Category(Enum):
    new_events = 'New Events'
    courses = 'Courses'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Article(models.Model):
    TITLE_MAX_LEN = 100
    CATEGORY_MAX_LEN = 20

    """
    To Do:
    to change 'author' to show in admin panel with 'full name' not with 'e-mail'
    """

    author = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        # null=True,
        # related_name='posts',
    )
    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=Category.choices(),
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
    )
    intro = models.TextField()
    body = models.TextField(
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + '|' + str(self.author.name)



