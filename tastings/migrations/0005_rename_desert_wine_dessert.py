# Generated by Django 4.1.4 on 2023-01-03 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tastings', '0004_tastingnote_thoughts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wine',
            old_name='desert',
            new_name='dessert',
        ),
    ]