# Generated by Django 4.1.4 on 2023-01-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_initialsurveyresponse_pay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initialsurveyresponse',
            name='meeting_preference',
        ),
        migrations.RemoveField(
            model_name='initialsurveyresponse',
            name='oneglassorseveral',
        ),
        migrations.RemoveField(
            model_name='initialsurveyresponse',
            name='pay',
        ),
        migrations.AddField(
            model_name='initialsurveyresponse',
            name='favoritewine',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
