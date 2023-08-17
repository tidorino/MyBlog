from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        user.groups.filter(name=group).exists()
    except Group.DoesNotExist:
        raise Exception(f"Group '{group_name}' does not exist.")
