# Generated by Django 2.2.7 on 2019-11-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_student_contest'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(blank=True, max_length=145, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(blank=True, max_length=145, null=True),
        ),
    ]
