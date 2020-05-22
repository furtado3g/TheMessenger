# Generated by Django 3.0.6 on 2020-05-22 16:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.IntegerField()),
                ('date_include', models.DateTimeField(default=datetime.datetime(2020, 5, 22, 16, 17, 5, 453180, tzinfo=utc))),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.AuthUser')),
            ],
        ),
    ]
