# Generated by Django 4.2.17 on 2025-03-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyserver_getcheesy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheesyjoke',
            name='repeat_interval',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cheesyquote',
            name='repeat_interval',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='compliment',
            name='repeat_interval',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
