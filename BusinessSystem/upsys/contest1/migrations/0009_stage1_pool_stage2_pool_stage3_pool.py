# Generated by Django 2.2.7 on 2020-01-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest1', '0008_contest1_is_review_by_stage1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage1_pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage1_pool', models.CharField(max_length=700, null=True, verbose_name='厅室审核池')),
            ],
        ),
        migrations.CreateModel(
            name='Stage2_pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage2_pool', models.CharField(max_length=700, null=True, verbose_name='校律委审核池')),
            ],
        ),
        migrations.CreateModel(
            name='Stage3_pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage3_pool', models.CharField(max_length=700, null=True, verbose_name='团委审核池')),
            ],
        ),
    ]
