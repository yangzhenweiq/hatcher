# Generated by Django 2.2.3 on 2020-05-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabulation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hatchrecord',
            name='out_machine',
            field=models.CharField(max_length=32, verbose_name='出壳机'),
        ),
    ]
