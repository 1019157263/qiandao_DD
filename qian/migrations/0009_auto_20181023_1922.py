# Generated by Django 2.1.1 on 2018-10-23 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qian', '0008_auto_20180929_0915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False, 'verbose_name_plural': '用户'},
        ),
    ]