# Generated by Django 3.0.2 on 2020-01-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorship', '0002_auto_20200122_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='valid',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
