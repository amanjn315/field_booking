# Generated by Django 2.1.7 on 2019-03-26 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20190323_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field_book',
            name='Mobile_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='field_book',
            name='date',
            field=models.DateField(default=datetime.date(2019, 3, 26)),
        ),
        migrations.AlterField(
            model_name='field_book',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='field_book',
            name='field',
            field=models.CharField(choices=[('CF', 'Cricket Field'), ('FF', 'Football Field'), ('BMC', 'Badminton Court'), ('BBC', 'Basketball Court'), ('HF', 'Hockey Field'), ('TC', 'Tennis Court'), ('AF', 'Athletic Field'), ('VC', 'Vollyball Court')], default=None, max_length=128),
        ),
    ]
