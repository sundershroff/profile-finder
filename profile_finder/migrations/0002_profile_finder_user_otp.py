# Generated by Django 4.1.6 on 2023-04-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_finder',
            name='user_otp',
            field=models.CharField(blank=True, default=None, max_length=6, null=True),
        ),
    ]
