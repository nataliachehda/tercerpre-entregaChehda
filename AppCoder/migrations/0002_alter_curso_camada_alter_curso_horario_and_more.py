# Generated by Django 4.2.2 on 2023-06-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='curso',
            name='horario',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='entregable',
            name='fecha',
            field=models.CharField(max_length=30),
        ),
    ]
