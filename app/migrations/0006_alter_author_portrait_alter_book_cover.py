# Generated by Django 4.0.4 on 2022-04-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_author_portrait_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='portrait',
            field=models.ImageField(default='defaultPortrait.jpg', upload_to='portraits/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='defaultCover.jpg', upload_to='covers/'),
        ),
    ]
