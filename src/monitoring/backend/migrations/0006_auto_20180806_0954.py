# Generated by Django 2.1 on 2018-08-06 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_devicereport_modified'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='device',
            table='device',
        ),
        migrations.AlterModelTable(
            name='devicereport',
            table='device_report',
        ),
    ]