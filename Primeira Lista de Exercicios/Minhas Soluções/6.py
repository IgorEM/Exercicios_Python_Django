
POPULACAO_A= float(input("Insira a população de A:"))
while POPULACAO_A <= 0:
    print("População de A não pode ser menor ou igual a 0 ")
    POPULACAO_A= float(input("Insira a população de A:"))

POPULACAO_B= float(input("Insira a população de B:"))
while POPULACAO_B <= 0:
    print("População de B não pode ser menor ou igual a 0 ")
    POPULACAO_B= float(input("Insira a população de B:"))

TX_A= float(input("Insira a Taxa de A: "))
while TX_A <= 0:
    print("Taxa de crescimento de A não pode ser menor que 0 ")
    TX_A= float(input("Insira a Taxa de A: "))

TX_B= float(input("Insira a Taxa de B: "))
while TX_B <= 0:
    print("Taxa de crescimento de B não pode ser menor que 0 ")
    TX_B= float(input("Insira a Taxa de B: "))


cont_anos = 0



while POPULACAO_A <= POPULACAO_B:
    porcentagemA = POPULACAO_A * TX_A
    porcentagemB = POPULACAO_B * TX_B

    print("porcentagemA: {}".format(porcentagemA))
    print("porcentagemB: {}".format(porcentagemB))


    POPULACAO_A = POPULACAO_A + porcentagemA
    POPULACAO_B = POPULACAO_B + porcentagemB

    print("POPULACAO_A: {}".format(POPULACAO_A))
    print("POPULACAO_B: {}".format(POPULACAO_B))

    cont_anos += 1
    print("anos: {}".format(cont_anos))
