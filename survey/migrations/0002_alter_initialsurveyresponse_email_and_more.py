# Generated by Django 4.1.4 on 2023-01-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialsurveyresponse',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='What is your Bowdoin email address?'),
        ),
        migrations.AlterField(
            model_name='initialsurveyresponse',
            name='meeting_preference',
            field=models.IntegerField(choices=[(0, 'Weekly'), (1, 'Biweekly'), (2, 'Monthly')], verbose_name='How often would you like to meet?'),
        ),
        migrations.AlterField(
            model_name='initialsurveyresponse',
            name='name',
            field=models.CharField(max_length=200, verbose_name='What is your name?'),
        ),
        migrations.AlterField(
            model_name='initialsurveyresponse',
            name='oneglassorseveral',
            field=models.IntegerField(choices=[(0, 'One glass of one wine'), (1, 'One glass of a selection of wines'), (2, 'Several small pours')], verbose_name='Would you prefer to drink one glass of a selected wine, one glass of your choice of a selection of wines, or several smaller pours of multiple wines?'),
        ),
        migrations.AlterField(
            model_name='initialsurveyresponse',
            name='pay',
            field=models.IntegerField(choices=[(0, '$0'), (1, '$1-$5'), (2, '$6-$10')], verbose_name='How much would you be willing to pay to attend?'),
        ),
    ]
