# Generated by Django 3.2.9 on 2021-12-15 11:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_whish'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Whish',
            new_name='Wish',
        ),
    ]