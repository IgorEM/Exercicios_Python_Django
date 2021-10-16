# Generated by Django 3.2.7 on 2021-10-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_people_signo'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='cep',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='cidade',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='endereco',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='estado',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='pais',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='tipo_sanguineo',
            field=models.CharField(max_length=10),
        ),
    ]