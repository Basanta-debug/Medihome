# Generated by Django 3.2.5 on 2021-08-10 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_auto_20210802_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.department'),
        ),
    ]
