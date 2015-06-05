# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150603_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.IntegerField(default=1, max_length=9, choices=[(1, b'Published'), (2, b'Hidden')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=1, max_length=9, choices=[(1, b'Published'), (2, b'Hidden')]),
        ),
        migrations.AlterField(
            model_name='slide',
            name='status',
            field=models.IntegerField(default=1, max_length=9, choices=[(1, b'Published'), (2, b'Hidden')]),
        ),
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.IntegerField(default=1, max_length=9, choices=[(1, b'Published'), (2, b'Hidden')]),
        ),
    ]
