# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-12 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_auto_20170512_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tgt_moni_info',
            name='queue_id',
            field=models.ForeignKey(db_column=b'queue_id', on_delete=django.db.models.deletion.CASCADE, to='orm.rep_queue', verbose_name='\u961f\u5217ID\u4fe1\u606f'),
        ),
    ]
