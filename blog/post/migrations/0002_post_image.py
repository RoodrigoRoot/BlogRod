# Generated by Django 3.0.8 on 2020-07-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='post', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]