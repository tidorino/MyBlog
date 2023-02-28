# Generated by Django 4.1.3 on 2023-02-20 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0012_alter_article_post_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_blog', '0002_delete_infoaboutapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
