# Generated by Django 2.2.7 on 2019-11-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20191117_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='TID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
