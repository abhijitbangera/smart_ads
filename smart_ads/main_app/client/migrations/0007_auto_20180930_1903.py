# Generated by Django 2.1.1 on 2018-09-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_adsdetails_update_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsdetails',
            name='update_flag',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]