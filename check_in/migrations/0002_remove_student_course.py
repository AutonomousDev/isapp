# Generated by Django 3.2.6 on 2021-12-04 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check_in', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
    ]