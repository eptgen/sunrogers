# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('img', models.ImageField(upload_to='comics/')),
                ('title', models.CharField(max_length=100)),
                ('alt', models.CharField(max_length=300)),
                ('date_done', models.DateField()),
            ],
        ),
    ]
