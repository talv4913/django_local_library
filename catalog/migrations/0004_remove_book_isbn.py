# Generated by Django 5.1.7 on 2025-04-02 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_book_author_alter_book_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
    ]
