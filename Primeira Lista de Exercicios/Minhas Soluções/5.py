POPULACAO_A = 80000 #crescimento anual de 3%
POPULACAO_B = 200000 #crescimento anual de 1.5%
TX_A= 0.30
TX_B= 0.015
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
