# Generated by Django 2.1.1 on 2018-09-30 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_auto_20180930_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsdetails',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]