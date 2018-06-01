# Generated by Django 2.0.1 on 2018-02-05 17:27

from django.db import migrations
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20171001_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='speaker_info',
            field=i18nfield.fields.I18nCharField(blank=True, help_text='Information relevant for speakers scheduled in this room, for example room size, special directions, available adapters for video input …', max_length=1000, null=True, verbose_name='Speaker Information'),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=i18nfield.fields.I18nCharField(blank=True, help_text='A description for attendees, for example directions.', max_length=1000, null=True, verbose_name='Description'),
        ),
    ]
