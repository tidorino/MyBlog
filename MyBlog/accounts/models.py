from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from MyBlog.accounts.managers import BlogUserManager
from MyBlog.core.validators import validate_only_letters


class BlogUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = BlogUserManager()


class Profile(models.Model):

    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    profile_image = models.URLField(
        null=False,
        blank=False,
    )

    user = models.OneToOneField(
        BlogUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'







