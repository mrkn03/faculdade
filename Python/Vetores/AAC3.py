#DETERMINAR OS VETORES
contas = []
saldos = []

while True:
    #MOSTRAR AS OPÇÕES DE OPERAÇÕES PARA O CLIENTE
    print(" "*5,"MENU PRINCIPAL"," "*5)
    print() #PULAR UMA LINHA
    print("CADASTRAR CONTA"," "*5, "[1]")
    print("SACAR", " "*15, "[2]")
    print("DEPOSITAR", " "*11, "[3]")
    print("VISUALIZAR SALDO", " "* 4, "[4]")
    print("SAIR", " "*16, "[5]")
    print() #PULAR UMA LINHA

    #PEDIR QUE O CLIENTE SOLICITE O TIPO DE OPERAÇÃO
    escolha = int(input("POR FAVOR ESCOLHA A OPERAÇÃO QUE DESEJA FAZER: "))
    
    #EFETUAR A OPÇÃO 1
    if escolha == 1:
        #PEDIR O NÚMERO DA CONTA E O VALOR INICIAL A SER DEPOSITADO
        numero_conta = int(input("DIGITE O NUMERO DA CONTA: "))
        saldo_inicial = float(input("DIGITE O SALDO INICIAL DA CONTA: R$"))

        #VERIFICAR SE A CONTA JÁ EXISTE
        if numero_conta in contas:
            print("CONTA JÁ EXISTENTE. TENTE NOVAMENTE.")
            continue

        #EFETUAR O CADASTRO DA CONTA E INSERIR O SALDO INICIAL
        contas.append(numero_conta)
        saldos.append(saldo_inicial)
        print("CADASTRO EFETUADO COM SUCESSO.")
        print() #PULAR UMA LINHA APÓS OPERAÇÃO

    #EFETUAR A OPÇÃO 2
    elif escolha == 2:
        #PEDIR O NÚMERO DA CONTA E O VALOR QUE DESEJA SER SACADO
        numero_conta = int(input("DIGITE O NÚMERO DA CONTA: "))
        valor_saque = float(input("DIGITE O VALOR QUE DESEJA SACAR: R$"))

        #CRIAR UM INDICE PARA RECEBER A LOCALIZAÇÃO NO VETOR DA CONTA INFORMADA
        indice_conta = contas.index(numero_conta)

        #VERIFICAR SE A CONTA INFORMADA NÃO EXISTE A PARTIR DO VETOR CONTAS
        if indice_conta == -1:
            print("CONTA NÃO EXISTENTE.")
            continue

        #SALDO RECEBE O SALDO ALOCADO NO INDICE DA CONTA INDICADA 
        saldo = saldos[indice_conta]

        #VERIFICAR SE É POSSÍVEL EFETUAR O SAQUE
        if saldo < valor_saque:
            print("SALDO INSUFICIENTE.")

        #EFETUAR O SAQUE E IMPRIMIR O SALDO ATUAL
        saldos[indice_conta] -= valor_saque
        print(f"SAQUE REALIZADO COM SUCESSO. SALDO ATUAL: R${saldos[indice_conta]}")
        print() #PULAR UMA LINHA APÓS OPERAÇÃO

    #EFETUAR A OPÇÃO 3
    elif escolha == 3:
        #PEDIR O NÚMERO DA CONTA E O VALOR QUE DESEJA DEPOSITAR
        numero_conta = int(input("DIGITE O NÚMERO DA CONTA: "))
        valor_deposito = float(input("DIGITE O VALOR QUE DESEJA DEPOSITAR: R$"))

        #CRIAR UM INDICE PARA RECEBER A LOCALIZAÇÃO NO VETOR DA CONTA INFORMADA
        indice_conta = contas.index(numero_conta)

        #VERIFICAR SE A CONTA INFORMADA NÃO EXISTE A PARTIR DO VETOR CONTAS
        if indice_conta == -1:
            print("CONTA NÃO EXISTENTE.")
            continue
        
        #EFETUAR O DEPÓSITO E IMPRIMIR O SALDO ATUAL
        saldo = saldos[indice_conta]
        saldo += valor_deposito
        saldos[indice_conta] = saldo
        print(f"DEPÓSITO REALIZADO COM SUCESSO. SALDO ATUAL: R${saldos[indice_conta]}")
        print() #PULAR UMA LINHA APÓS OPERAÇÃO

    #EFETUAR A OPÇÃO 4
    elif escolha == 4:
        #PEDIR O NÚMERO DA CONTA
        numero_conta = int(input("DIGITE O NÚMERO DA CONTA: "))

        #CRIAR UM INDICE PARA RECEBER A LOCALIZAÇÃO NO VETOR DA CONTA INFORMADA
        indice_conta = contas.index(numero_conta)

        #VERIFICAR SE A CONTA INFORMADA NÃO EXISTE A PARTIR DO VETOR CONTAS
        if indice_conta == -1:
            print("CONTA NÃO EXISTE.")
            continue
        
        #SALDO RECEBE O VALOR ALOCADO NA CONTA INFORMADA E INFORMA AO CLIENTE O SALDO ATUAL
        saldo = saldos[indice_conta]
        print(f"SALDO ATUAL: R${saldo}")
        print() #PULAR UMA LINHA APÓS OPERAÇÃO

    #EFETUAR A OPÇÃO 5
    elif escolha == 5:
        print("ENCERRANDO PROGRAMA...")
        break
    
    #SE USUÁRIO DIGITAR QUALQUER NÚMERO DIFERENTE DE 1 A 5
    else:
        print("OPERAÇÃO INVÁLIDA. TENTE NOVAMENTE. ")
        print() #PULAR UMA LINHA APÓS OPERAÇÃO





