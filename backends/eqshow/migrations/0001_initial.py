# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EqshowPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enterprise', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
            ],
        ),
    ]
