# Generated by Django 2.0 on 2018-12-11 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Scheduling', '0002_auto_20181204_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchedulePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='availability',
            name='employee',
        ),
        migrations.AddField(
            model_name='availability',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]