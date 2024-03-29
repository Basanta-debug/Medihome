# Generated by Django 3.2.6 on 2021-08-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_auto_20210727_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fullname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
