# Generated by Django 3.2.8 on 2021-10-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_cartorios_nome_oficial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorios',
            name='area_de_abrangencia',
            field=models.CharField(max_length=201),
        ),
    ]
