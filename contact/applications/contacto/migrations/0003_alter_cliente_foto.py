# Generated by Django 4.1.3 on 2024-03-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_alter_cliente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='contacto'),
        ),
    ]
