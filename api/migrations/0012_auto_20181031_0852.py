# Generated by Django 2.1.1 on 2018-10-31 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181029_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='orden',
        ),
        migrations.RemoveField(
            model_name='seccion',
            name='orden',
        ),
    ]
