# Generated by Django 3.1.14 on 2022-04-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins_app', '0010_auto_20220404_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='name',
            field=models.CharField(help_text='Rozeznávací jméno služby, musí být unikátní.', max_length=64),
        ),
    ]
