# Generated by Django 3.1.14 on 2022-04-04 17:32

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('plugins_app', '0006_auto_20220404_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='plugins_app_servicesmodel', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(default='Služby', help_text='Titulek služeb.', max_length=64)),
                ('cards', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='service_cards', to='cms.placeholder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
