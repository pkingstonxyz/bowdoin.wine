# Generated by Django 4.1.4 on 2023-01-21 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tastings', '0005_rename_desert_wine_dessert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='dessert',
        ),
    ]