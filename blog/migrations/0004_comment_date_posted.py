# Generated by Django 4.1.7 on 2023-03-28 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
