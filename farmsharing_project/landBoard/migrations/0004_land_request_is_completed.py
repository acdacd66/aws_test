# Generated by Django 2.2.7 on 2019-11-27 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landBoard', '0003_remove_land_request_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='land_request',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]