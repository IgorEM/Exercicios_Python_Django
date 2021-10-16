# Desafio
Usando a API de modelos do Django, elabore queries para atender as seguintes operações

### 1. Uma lista das n pessoas mais jovens, ordenadas ascendentementem
PeMaJoOrAs = People.objects.order_by('-data_nasc')
### 2.Uma lista das n pessoas mais velhas ordenadas ascendentemente
PeMaVeOrAs = People.objects.order_by('data_nasc')
### 3.Qual a quantidade de pessoas do sexo feminino?
fem = People.objects.filter(sexo="F").count()
### 4.Qual a quantidade de pessoas do sexo masculino?
mas = People.objects.filter(sexo="M").count()
### 5.Escreva uma método "to_json", que retorne os dados de uma pessoa em formato json
People.objects.to_json(8) #criado em models
### 6.Listar os nomes de todas as pessoas no dataset em ordem alfabética
nomes_ord_alf = People.objects.values('nome').order_by('nome')
### 7.Implemente uma função para buscar pessoas por nome, ou parte do nome (Case insensitive)
People.objects.contem("cio") #criado em models