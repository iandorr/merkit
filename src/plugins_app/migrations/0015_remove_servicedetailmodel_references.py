# Generated by Django 3.1.14 on 2022-11-02 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plugins_app', '0014_merkitnavbarmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedetailmodel',
            name='references',
        ),
    ]
