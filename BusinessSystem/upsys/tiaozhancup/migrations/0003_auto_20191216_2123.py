# Generated by Django 2.2.7 on 2019-12-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiaozhancup', '0002_auto_20191216_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiaozhancup',
            name='is_fail',
            field=models.BooleanField(default=False, null=True, verbose_name='is_fail'),
        ),
        migrations.AddField(
            model_name='tiaozhancup',
            name='is_pass',
            field=models.BooleanField(default=False, null=True, verbose_name='is_pass'),
        ),
        migrations.AddField(
            model_name='tiaozhancup',
            name='is_reviewing',
            field=models.BooleanField(default=True, null=True, verbose_name='is_reviewing'),
        ),
    ]
