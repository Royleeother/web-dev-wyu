# Generated by Django 2.2.7 on 2019-11-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_teacher_authorization_for_contest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contest',
            field=models.CharField(blank=True, default='[]', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='authorization_for_contest',
            field=models.CharField(blank=True, default='[]', max_length=500, null=True),
        ),
    ]