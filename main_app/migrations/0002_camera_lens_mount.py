# Generated by Django 4.0.4 on 2022-04-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='lens_mount',
            field=models.CharField(default='Fujifilm X', max_length=50),
            preserve_default=False,
        ),
    ]
