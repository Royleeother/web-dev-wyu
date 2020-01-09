# Generated by Django 2.2.7 on 2019-11-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest1', '0003_auto_20191123_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest1',
            name='ccyl_opnion',
        ),
        migrations.RemoveField(
            model_name='contest1',
            name='discipline_unit_opnion',
        ),
        migrations.RemoveField(
            model_name='contest1',
            name='guiding_unit_opnion',
        ),
        migrations.AddField(
            model_name='contest1',
            name='ccyl_decision',
            field=models.BooleanField(null=True, verbose_name='团委决定'),
        ),
        migrations.AddField(
            model_name='contest1',
            name='discipline_unit_decision',
            field=models.BooleanField(null=True, verbose_name='校律委决定'),
        ),
        migrations.AddField(
            model_name='contest1',
            name='guiding_unit_decision',
            field=models.BooleanField(null=True, verbose_name='厅室管理员决定'),
        ),
    ]
