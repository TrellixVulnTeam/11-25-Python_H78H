# Generated by Django 2.2 on 2019-12-10 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='release_date',
        ),
    ]
