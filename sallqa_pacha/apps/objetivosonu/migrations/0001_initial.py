# Generated by Django 3.0 on 2021-12-13 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to='imagenes_ods')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=40)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=1500)),
                ('imagen', models.ImageField(upload_to='imagenes_post')),
                ('ods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objetivosonu.Ods')),
            ],
        ),
    ]
