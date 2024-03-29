from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from MyBlog.accounts.models import Profile
from MyBlog.core.validators import validate_max_image_size


UserModel = get_user_model()


class Category(models.Model):
    CATEGORY_MAX_LEN = 20

    name = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    TITLE_MAX_LEN = 100
    CATEGORY_MAX_LEN = 20
    SLUG_MAX_LEN = 100

    PUBLISHED = 'Published'
    DRAFT = 'Draft'

    STATUS = (
        (0, DRAFT),
        (1, PUBLISHED),
    )

    author = models.ForeignKey(
        to=Profile,
        # 'Restrict - we can't delete author as he is connected to article
        on_delete=models.CASCADE,
        related_name='articles',
        null=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    # null=False, blank=True, if we don't write slug ,automatically to be 'null' and 'save'
    # function to generate 'slug'
    slug = models.SlugField(
        max_length=SLUG_MAX_LEN,
        unique=True,
        null=False,
        blank=True,
    )

    body = RichTextField(
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    post_image = models.ImageField(
        upload_to='articles/',
        null=False,
        blank=False,
        validators=(
            validate_max_image_size,
        )
    )
    status = models.IntegerField(

        choices=STATUS,
        default=0,
        null=True,
        blank=True,
    )
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    # To do that, we will override the Article model save() method using a special function called slugify()
    # which helps us structure a slug from a given value.
    # The if-statement     stands to say that the slug field will NOT be changed
    # when the name of the article is changed:
    def save(self, *args, **kwargs):
        # create/update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.title}')

        # update
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}' + '|' + f'{self.author}'


class ArticleLike(models.Model):
    post = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='post_likes',
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='user_likes'
    )
