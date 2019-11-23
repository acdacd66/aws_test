# Generated by Django 2.2.7 on 2019-11-23 12:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('otherBoard', '0002_review_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='scrap',
            field=models.ManyToManyField(blank=True, related_name='Profile_scrap', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='Profile_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
