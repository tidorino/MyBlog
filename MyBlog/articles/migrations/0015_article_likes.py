# Generated by Django 4.1.7 on 2023-08-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_alter_article_body_alter_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]