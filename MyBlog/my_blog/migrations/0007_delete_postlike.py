# Generated by Django 4.1.7 on 2023-08-15 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0006_postlike'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]