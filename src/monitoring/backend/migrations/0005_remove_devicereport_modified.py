# Generated by Django 2.1 on 2018-08-06 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_devicereport_last_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicereport',
            name='modified',
        ),
    ]
