# Generated by Django 2.2 on 2019-09-28 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adduser',
            name='CPassword',
        ),
    ]
