# Generated by Django 3.0.5 on 2022-01-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_auto_20220114_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprescriptiondetails',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
