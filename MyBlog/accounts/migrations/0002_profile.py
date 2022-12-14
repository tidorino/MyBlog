# Generated by Django 4.1.3 on 2022-12-05 09:28

import MyBlog.core.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), MyBlog.core.validators.validate_only_letters])),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), MyBlog.core.validators.validate_only_letters])),
                ('profile_image', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
