# Generated by Django 4.1.3 on 2022-12-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.IntegerField(blank=True, choices=[('Published', 1), ('Draft', 0)],
                                      default=1, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
