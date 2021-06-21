# Generated by Django 3.2.4 on 2021-06-21 03:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0003_auto_20210621_0011'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together={('event', 'participant'), ('participant', 'drawn')},
        ),
    ]