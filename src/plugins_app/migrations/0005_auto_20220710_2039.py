# Generated by Django 3.1.14 on 2022-07-10 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plugins_app', '0004_delete_linkmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plugins_app.linkmanager'),
        ),
        migrations.AlterField(
            model_name='maininfomodel',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plugins_app.linkmanager'),
        ),
        migrations.AlterField(
            model_name='servicesmodel',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plugins_app.linkmanager'),
        ),
        migrations.AlterField(
            model_name='welcomemodel',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plugins_app.linkmanager'),
        ),
    ]
