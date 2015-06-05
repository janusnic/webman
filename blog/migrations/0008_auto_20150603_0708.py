# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Dratf'), (b'1', b'Published'), (b'2', b'Not Published')])),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(max_length=1024, null=True, upload_to=blog.models.get_blog_file_name, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Dratf'), (b'1', b'Published'), (b'2', b'Not Published')])),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='slide',
            name='related_slider',
            field=models.ForeignKey(to='blog.Slider'),
        ),
    ]
