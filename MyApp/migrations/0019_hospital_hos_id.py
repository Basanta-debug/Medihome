# Generated by Django 3.2.5 on 2021-08-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0018_alter_appointment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='hos_id',
            field=models.IntegerField(null=True),
        ),
    ]
