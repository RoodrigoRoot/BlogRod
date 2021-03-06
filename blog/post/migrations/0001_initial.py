# Generated by Django 3.0.8 on 2020-07-21 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile', verbose_name='Perfil')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
    ]
