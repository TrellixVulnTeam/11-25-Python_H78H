# Generated by Django 2.2 on 2019-12-20 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clock_in_out_app', '0014_award_clock'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Award',
        ),
    ]