# Generated by Django 2.2.2 on 2019-06-07 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0002_book_is_avi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='is_avi',
            new_name='is_available',
        ),
    ]
