# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150509_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Dratf'), (b'1', b'Published'), (b'2', b'Not Published')]),
        ),
    ]
