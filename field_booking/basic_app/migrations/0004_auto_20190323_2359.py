# Generated by Django 2.1.7 on 2019-03-23 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20190323_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field_book',
            old_name='number',
            new_name='Mobile_number',
        ),
        migrations.AddField(
            model_name='field_book',
            name='date',
            field=models.DateField(default=datetime.date(2019, 3, 23)),
        ),
    ]