# Generated by Django 3.0.7 on 2020-07-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200717_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(blank=True, default='none', null=True),
        ),
    ]