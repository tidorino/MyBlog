# Generated by Django 4.1.7 on 2023-08-15 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0008_showbycategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShowByCategory',
        ),
    ]