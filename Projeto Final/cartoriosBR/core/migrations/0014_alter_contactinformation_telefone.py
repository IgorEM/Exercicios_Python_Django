# Generated by Django 3.2.8 on 2021-10-21 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_contactinformation_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation',
            name='telefone',
            field=models.CharField(max_length=50),
        ),
    ]