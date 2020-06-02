# Generated by Django 2.2.3 on 2020-05-26 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabulation', '0006_hatchrecord_beizhu'),
    ]

    operations = [
        migrations.CreateModel(
            name='HatchContrast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hatch_pattern', models.SmallIntegerField(choices=[(1, '冬温大蛋'), (2, '冬温小蛋'), (3, '夏温大蛋'), (4, '夏温小蛋')], verbose_name='孵化模式')),
                ('tailing', models.IntegerField(verbose_name='胎龄')),
                ('biaowen', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='标温')),
                ('tiaowen', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='调温')),
                ('cefengmen', models.CharField(max_length=32, verbose_name='侧风门')),
                ('shangfengmen', models.CharField(max_length=32, verbose_name='上风门')),
                ('shidu', models.IntegerField(verbose_name='湿度')),
                ('zhaodan', models.CharField(blank=True, max_length=255, null=True, verbose_name='照蛋')),
                ('luopan', models.CharField(blank=True, max_length=255, null=True, verbose_name='落盘')),
                ('other', models.CharField(blank=True, max_length=255, null=True, verbose_name='其他')),
            ],
        ),
        migrations.AlterField(
            model_name='hatchrecord',
            name='hatch_pattern',
            field=models.SmallIntegerField(choices=[(1, '冬温大蛋'), (2, '冬温小蛋'), (3, '夏温大蛋'), (4, '夏温小蛋')], default=3, verbose_name='孵化模式'),
        ),
    ]