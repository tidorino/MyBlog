# Generated by Django 4.1.3 on 2022-12-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(blank=True, choices=[('Published', 'Published'), ('Draft', 'Draft')], null=True),
        ),
    ]
