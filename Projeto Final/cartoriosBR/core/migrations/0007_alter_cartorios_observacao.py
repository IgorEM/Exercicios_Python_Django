# Generated by Django 3.2.8 on 2021-10-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_cartorios_atribuicoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorios',
            name='observacao',
            field=models.CharField(max_length=500),
        ),
    ]