# Generated by Django 3.2.8 on 2021-10-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adressess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8, null=True)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cartorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18)),
                ('cns', models.CharField(max_length=8)),
                ('data_de_instalacao', models.CharField(max_length=10)),
                ('nome_oficial', models.CharField(max_length=300)),
                ('nome_fantasia', models.CharField(blank=True, max_length=300, null=True)),
                ('nome_do_titular', models.CharField(max_length=100)),
                ('nome_do_substituto', models.CharField(max_length=100)),
                ('nome_do_juiz', models.CharField(max_length=100)),
                ('observacao', models.CharField(max_length=300)),
                ('ultima_atualizacao', models.CharField(max_length=300)),
                ('horario_de_funcionamento', models.CharField(max_length=300)),
                ('area_de_abrangencia', models.CharField(max_length=300)),
                ('atribuicoes', models.CharField(max_length=300)),
                ('comarca', models.CharField(max_length=300)),
                ('entrancia', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=17)),
                ('fax', models.CharField(max_length=100)),
            ],
        ),
    ]