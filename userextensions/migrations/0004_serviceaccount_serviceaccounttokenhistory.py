# Generated by Django 2.2.15 on 2020-10-16 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('userextensions', '0003_auto_20200117_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date/time when this row was first created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='date/time this row was last updated')),
                ('enabled', models.BooleanField(default=True, help_text='enable/disable state of user')),
                ('description', models.CharField(blank=True, help_text='optional description', max_length=254, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'group')},
            },
        ),
        migrations.CreateModel(
            name='ServiceAccountTokenHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='date/time when this token refresh occurred')),
                ('actor', models.ForeignKey(help_text='user who refreshed token', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('srv_acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userextensions.ServiceAccount')),
            ],
        ),
    ]
