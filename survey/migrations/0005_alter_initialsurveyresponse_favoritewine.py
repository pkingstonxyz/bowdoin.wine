# Generated by Django 4.1.4 on 2023-01-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_remove_initialsurveyresponse_meeting_preference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialsurveyresponse',
            name='favoritewine',
            field=models.CharField(blank=True, max_length=200, verbose_name='Favorite wine? (optional)'),
        ),
    ]
