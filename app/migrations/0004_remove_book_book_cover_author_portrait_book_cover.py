# Generated by Django 4.0.4 on 2022-04-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_cover',
        ),
        migrations.AddField(
            model_name='author',
            name='portrait',
            field=models.ImageField(default='defaultPortrait.jpg', upload_to='portraits/'),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='defaultCover.jpg', upload_to='covers/'),
        ),
    ]
