# Generated by Django 2.2.4 on 2019-09-06 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corus', '0023_auto_20190907_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='e_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='complain',
            name='u_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='odate',
            field=models.DateField(default=datetime.datetime(2019, 9, 7, 3, 13, 17, 626451)),
        ),
        migrations.AlterField(
            model_name='order',
            name='u_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transection',
            name='c_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transection',
            name='e_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transection',
            name='u_id',
            field=models.IntegerField(default=0),
        ),
    ]
