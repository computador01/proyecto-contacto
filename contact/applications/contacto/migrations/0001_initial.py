# Generated by Django 5.0.2 on 2024-02-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='portada')),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]