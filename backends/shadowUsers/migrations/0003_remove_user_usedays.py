# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shadowUsers', '0002_auto_20160123_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='useDays',
        ),
    ]
