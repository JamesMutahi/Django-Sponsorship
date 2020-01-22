# Generated by Django 3.0.2 on 2020-01-21 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=255)),
                ('applicant_address', models.CharField(max_length=255)),
                ('applicant_phone', models.IntegerField()),
                ('applicant_email', models.EmailField(max_length=254)),
                ('applicant_birth_cert', models.FileField(upload_to='birth_certs')),
                ('applicant_national_id', models.FileField(upload_to='national_ids')),
                ('school_name', models.CharField(max_length=255)),
                ('school_address', models.CharField(max_length=255)),
                ('academic_level', models.CharField(max_length=255)),
                ('year_of_completion', models.DateField()),
                ('reasons', models.TextField()),
                ('recommendation_letter', models.FileField(upload_to='recommendation_letters')),
                ('valid', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
