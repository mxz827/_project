# Generated by Django 2.2.12 on 2020-05-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Event Name'),
        ),
    ]