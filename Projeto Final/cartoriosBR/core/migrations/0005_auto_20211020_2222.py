# Generated by Django 3.2.8 on 2021-10-21 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211020_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorios',
            name='area_de_abrangencia',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='cartorios',
            name='atribuicoes',
            field=models.CharField(max_length=170),
        ),
        migrations.AlterField(
            model_name='cartorios',
            name='comarca',
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name='cartorios',
            name='entrancia',
            field=models.CharField(max_length=190),
        ),
        migrations.AlterField(
            model_name='cartorios',
            name='horario_de_funcionamento',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cartorios',
            name='nome_fantasia',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cartorios',
            name='nome_oficial',
            field=models.CharField(max_length=110),
        ),
        migrations.AlterField(
            model_name='cartorios',
            name='observacao',
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='cartorios',
            name='ultima_atualizacao',
            field=models.CharField(max_length=140),
        ),
    ]
