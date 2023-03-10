# Generated by Django 3.1.14 on 2022-07-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins_app', '0007_contactformmodel_button_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='text',
            field=models.TextField(blank=True, help_text='Text showcased under the title on the contact form.'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='title',
            field=models.CharField(default='Kontakt', help_text='Title of the contact form.', max_length=64),
        ),
        migrations.AlterField(
            model_name='maininfomodel',
            name='text',
            field=models.TextField(help_text='Text showcased in the main info section.'),
        ),
        migrations.AlterField(
            model_name='maininfomodel',
            name='title',
            field=models.CharField(default='Hlavní Informace', help_text='Title of the main info section.', max_length=64),
        ),
        migrations.AlterField(
            model_name='servicedetailmodel',
            name='text',
            field=models.TextField(help_text='Text describing the service.'),
        ),
        migrations.AlterField(
            model_name='servicedetailmodel',
            name='title',
            field=models.CharField(help_text='Title of the service detail.', max_length=64),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='back_text',
            field=models.TextField(help_text='Text on the back of the card.'),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='back_title',
            field=models.CharField(help_text='Title of the service on the back of the card.', max_length=64),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='name',
            field=models.CharField(help_text='Discerning name of the service, must be unique!', max_length=64),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='title',
            field=models.CharField(help_text='Title of the service.', max_length=64),
        ),
        migrations.AlterField(
            model_name='servicesmodel',
            name='title',
            field=models.CharField(default='Služby', help_text='Title of the services section.', max_length=64),
        ),
        migrations.AlterField(
            model_name='welcomemodel',
            name='welcome_text',
            field=models.CharField(default='Vítejte na Merkit', help_text='Main welcome text.', max_length=255),
        ),
    ]
