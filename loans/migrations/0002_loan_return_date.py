# Generated by Django 3.0.3 on 2020-02-16 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='return_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]