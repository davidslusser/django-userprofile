# Generated by Django 2.2.6 on 2019-12-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userextensions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreference',
            name='start_page',
            field=models.CharField(blank=True, help_text='url to redirect to after user login', max_length=255, null=True),
        ),
    ]