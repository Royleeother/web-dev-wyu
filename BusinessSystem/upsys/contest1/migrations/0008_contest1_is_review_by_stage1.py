# Generated by Django 2.2.7 on 2020-01-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest1', '0007_auto_20200106_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest1',
            name='is_review_by_stage1',
            field=models.BooleanField(default=False, null=True, verbose_name='厅室管理员正在审核'),
        ),
    ]
