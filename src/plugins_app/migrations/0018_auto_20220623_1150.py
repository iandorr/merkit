# Generated by Django 3.1.14 on 2022-06-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins_app', '0017_linkmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkmodel',
            name='href',
            field=models.CharField(help_text='ID sekce na kterou link odkazuje, ID začínají #, url /.', max_length=64),
        ),
    ]
