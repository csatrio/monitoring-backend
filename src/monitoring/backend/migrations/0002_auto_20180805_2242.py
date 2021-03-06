# Generated by Django 2.1 on 2018-08-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='password',
            field=models.CharField(default='1234', max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='device',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=9),
        ),
    ]
