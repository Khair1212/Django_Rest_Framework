# Generated by Django 4.0.5 on 2022-06-03 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='suthor',
            new_name='author',
        ),
    ]