# Generated by Django 3.1.14 on 2022-08-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins_app', '0012_auto_20220830_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='link_href',
            field=models.CharField(blank=True, help_text='ID that will be appended to the section, create a unique one please.', max_length=64),
        ),
        migrations.AlterField(
            model_name='maininfomodel',
            name='link_href',
            field=models.CharField(blank=True, help_text='ID that will be appended to the section, create a unique one please.', max_length=64),
        ),
        migrations.AlterField(
            model_name='servicesmodel',
            name='link_href',
            field=models.CharField(blank=True, help_text='ID that will be appended to the section, create a unique one please.', max_length=64),
        ),
        migrations.AlterField(
            model_name='welcomemodel',
            name='link_href',
            field=models.CharField(blank=True, help_text='ID that will be appended to the section, create a unique one please.', max_length=64),
        ),
    ]
