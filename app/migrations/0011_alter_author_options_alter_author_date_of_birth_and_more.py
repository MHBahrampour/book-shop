# Generated by Django 4.0.4 on 2022-05-04 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_shoppingcart_books_shoppingcart_books'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(null=True),
        ),
    ]
