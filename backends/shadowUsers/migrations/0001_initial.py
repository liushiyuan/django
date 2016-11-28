# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=150)),
                ('port', models.IntegerField()),
                ('price', models.IntegerField()),
                ('addDate', models.DateField()),
                ('useDays', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]
