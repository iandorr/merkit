# Generated by Django 3.1.14 on 2022-05-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins_app', '0014_auto_20220423_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcomemodel',
            name='link_id',
            field=models.CharField(default='welcome_section', help_text='ID sekce pro linkovací důvody.', max_length=64),
        ),
    ]
