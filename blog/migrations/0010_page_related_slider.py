# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150603_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='related_slider',
            field=models.ForeignKey(blank=True, to='blog.Slider', null=True),
        ),
    ]
