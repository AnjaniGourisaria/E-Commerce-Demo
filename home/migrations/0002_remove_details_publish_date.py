# Generated by Django 3.2.9 on 2021-12-03 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='publish_date',
        ),
    ]