# Generated by Django 3.1.4 on 2021-05-10 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210409_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]