# Generated by Django 3.2.20 on 2023-09-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersmanage', '0012_userdata_other_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='activated_by_admin',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='User activated by administrator'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='registered',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Registered user'),
        ),
    ]
