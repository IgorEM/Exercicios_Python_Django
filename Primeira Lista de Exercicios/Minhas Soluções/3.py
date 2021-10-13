nome = input("Insira seu nome: ")
a = list(nome)
cont = 0
for i in a:
    cont += 1

print(cont)
if cont > 3:
    print("Nome válido")
else:
    print("Nome invalido. O nome nao pode ter mais que 3 caracteres")


idade = int(input("Insira sua idade: "))
if (idade <= 150) or idade >= 0: 
    print("Idade válida") 
else:
    print("idade invalida. Digite uma idade entre 0 e 150.")


salario = float(input("insira seu salaário: "))
if salario > 0:
    print("Salario válido")
else:
    print("Salario Invalido.DIgite um salario maior que zero")

sexo = input("Insira seu sexo:")
if sexo == 'f' or sexo == 'm':
    print("sexo válido")
else:
    print('sexo inválido')

estado_civil = input("Insira seu estado civil: ")
if estado_civil in ("s", "c", "v", "d"):
    print("estado civil válido")
else:
    print("estado civil inválido")

