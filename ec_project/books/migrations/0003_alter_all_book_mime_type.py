# Generated by Django 4.2.11 on 2024-03-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_all_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_book',
            name='mime_type',
            field=models.CharField(max_length=255),
        ),
    ]