# Generated by Django 2.0 on 2018-12-25 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employment', '0002_auto_20181224_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='num_hours',
            field=models.IntegerField(default=0),
        ),
    ]
