# Generated by Django 3.2.7 on 2021-09-29 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=15)),
                ('data_nasc', models.DateTimeField()),
                ('sexo', models.CharField(max_length=10)),
                ('mae', models.CharField(max_length=150)),
                ('pai', models.CharField(max_length=150)),
                ('celular', models.CharField(max_length=150)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=3)),
                ('peso', models.PositiveIntegerField()),
                ('tipo_sanguineo', models.CharField(max_length=4)),
            ],
        ),
    ]
