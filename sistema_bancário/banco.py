# saque deposito extrato 
#depósito positivo devem ser exibidos na operação de extrato
#saque 3 saques  diários, 500 reais de limite, mensagem de erro em caso de saldo insuficiente
menu = """
***********************
        Menu
[0]Sair
[1]Extrato
[2]Saque
[3]Depósito  
***********************\n
"""
saldo=0
limite=500
extrato = ""
numero_saques=0
LIMITE_SAQUES =3 

while True:
    opcao = int(input(menu))
    if opcao == 1:
        print("===============EXTRATO===============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print(f"==============================")
    elif opcao == 2:
        saque=int(input("Informe o valor do saque: "))
        if saque> 0 and saque<=saldo and saque<=limite and numero_saques<LIMITE_SAQUES:
            print("Saque realizado")
            saldo-=saque
            numero_saques+=1
            extrato+= f"\nSaque realizado: R${saque: .2f}"
        else:
            if saque<=0:
                print("Saque inválido")
            elif saque>saldo:
                print("Saldo Insuficiente")
            elif saque>=limite:
                print("Limite de saque excedido, por favor, insira um novo valor até R$ 500.00")
            else:
                print("Limite de saques diários atingido")
    elif opcao==3:
        deposito=int(input("Informe o valor do depósito: "))
        if deposito>0:
            saldo+= deposito
            extrato+= f"\nDepósito realizado: R$ {deposito: .2f}"
        else:
            print("Depósito Inválido")
    elif opcao==0:
        print("Encerrando operação")
        break
    else:
        print("Opção inválida")

