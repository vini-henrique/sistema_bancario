opcao = int(input("Escolha a opção: [1]Saldo [2]Saque [3]Depósito [0]Sair \n"))
print(opcao)
saldo=0

while(opcao!= 0):
    if opcao == 1:
        print("Consultar Saldo")
        opcao = int(input("Escolha a opção: [1]Saldo [2]Saque [3]Depósito\n"))
    elif opcao == 2:
        saque=int(input("Informe o valor do saque: "))
        if saque<saldo:
            print("Saque realizado")
            opcao = int(input("Escolha a opção: [1]Saldo [2]Saque [3]Depósito\n"))
        else:
            print("Saldo insuficiente")
            opcao = int(input("Escolha a opção: [1]Saldo [2]Saque [3]Depósito\n"))
    elif opcao==3:
        deposito=int(input("Informe o valor do depósito: "))
        saldo= saldo + deposito
        print(saldo)
        opcao = int(input("Escolha a opção: [1]Saldo [2]Saque [3]Depósito\n"))
    elif opcao==0:
        print("Encerrando operação")
    else:
        print("Opção inválida")
        opcao = int(input("Escolha a opção: [1]Saldo [2]Saque [3]Depósito\n"))