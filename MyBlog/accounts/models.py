from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from MyBlog.accounts.managers import BlogUserManager
from MyBlog.core.validators import validate_only_letters


class BlogUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = BlogUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):

    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    user = models.OneToOneField(
        BlogUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='profile'
    )  # user_id => 'profile_instance.pk' will work

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    profile_image = models.URLField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


