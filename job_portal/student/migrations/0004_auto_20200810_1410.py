# Generated by Django 3.1 on 2020-08-10 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200810_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='responsibilites',
            new_name='responsibilities',
        ),
    ]