# Generated by Django 4.1.6 on 2023-05-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_finder', '0014_cities'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_finder',
            name='dob',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
