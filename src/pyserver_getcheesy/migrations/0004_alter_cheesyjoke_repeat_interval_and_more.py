# Generated by Django 4.2.17 on 2025-03-11 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyserver_getcheesy', '0003_alter_cheesyjoke_repeat_interval_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheesyjoke',
            name='repeat_interval',
            field=models.DateTimeField(blank=True, default=datetime.timedelta(days=1), null=True),
        ),
        migrations.AlterField(
            model_name='cheesyquote',
            name='repeat_interval',
            field=models.DateTimeField(blank=True, default=datetime.timedelta(days=1), null=True),
        ),
        migrations.AlterField(
            model_name='compliment',
            name='repeat_interval',
            field=models.DateTimeField(blank=True, default=datetime.timedelta(days=1), null=True),
        ),
    ]
