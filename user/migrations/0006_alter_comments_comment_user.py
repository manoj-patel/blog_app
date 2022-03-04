# Generated by Django 4.0.2 on 2022-03-03 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0005_remove_comments_name_comments_comment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
