from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from MyBlog.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
