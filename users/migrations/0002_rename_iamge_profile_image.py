# Generated by Django 4.2.7 on 2023-11-13 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='iamge',
            new_name='image',
        ),
    ]
