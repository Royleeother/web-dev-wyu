# Generated by Django 2.2.7 on 2019-11-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest1', '0002_auto_20191122_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest1',
            name='ccyl_comment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contest1',
            name='discipline_unit_comment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contest1',
            name='guiding_unit_comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]