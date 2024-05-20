import re

menu = """---------------------
MENU
[1] EXTRATO
[2] DEPÓSITO
[3] SAQUE
[4] USUÁRIO
[5] CONTA-CORRENTE
[6] EXIBIR CONTAS CADASTRADAS
[0] SAIR
---------------------
"""


def checar_extrato(saldo, /, *, extrato):
    #retorna o extrato ao usuário, sendo atualizado a cada saque ou depósito
    print('----------EXTRATO----------')
    print(extrato if extrato else 'Não foram realizadas movimentações.')
    print(f'\nSaldo: R${saldo:.2f}')
    print('---------------------------')


def deposito(saldo, extrato,/):
    '''Realiza o depósito do usuário desde que o valor seja superior a zero, retornando o valor para a função principal'''
    valor = float(input('Digite o valor do depósito: '))
    if valor > 0:
        saldo += valor
        print('Depósito realizado com sucesso.')
        extrato += f'\nDepósito: R${valor:.2f}'
    else:
        print('Valor inválido.')
    return saldo, extrato


def saque(*, saldo, extrato, limite, LIMITE_SAQUES, numero_saques):
    '''Realiza o saque do usuário desde que o valor seja superior a zero, retornando o valor para a função principal e atualizando o número de saques diários'''
    valor = float(input('Digite o valor do saque: '))
    saldo_insuficiente = valor > saldo
    saque_invalido = valor <= 0
    limite_excedido = valor > limite
    limite_diario = numero_saques >= LIMITE_SAQUES
    if saldo_insuficiente:
        print('Saldo insuficiente.')

    elif saque_invalido:
        print('Saque inválido.')
    elif limite_excedido:
        print('Saque mal-sucedido. Superior ao limite.')
    elif limite_diario:
        print('Número máximo de saques diários atingido.')
    else:
        saldo -= valor
        extrato += f'\nSaque: R${valor:.2f}'
        print('Saque realizado. Obrigado por usar nossos serviços.')
        numero_saques += 1
    return saldo, extrato, numero_saques


def criar_usuario(usuarios):
    #Cria ausuário com base em funções de validação e retorna à função principal
    cpf = validar_cpf()
    usuario = validar_usuario(usuarios, cpf)
    if usuario:
        print('Usuário já cadastrado.')
        return

    nome = validar_nome()
    endereco = validar_endereco()
    data_nascimento = validar_nascimento()

    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'endereco': endereco,
        'data_nascimento': data_nascimento
    })
    print('Usuário cadastrado com sucesso.')


def validar_cpf():
    #Valida o CPF do usuário
    while True:
        cpf = input('Informe o seu CPF(000.000.000-00): ')
        if re.search(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$', cpf):
        break
        else:
        print('CPF inválido.')
    return cpf


def validar_nascimento():
    #valida a data de nascimento do usuário
    while True:
        data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
        if re.search(r'^[0-9]{2}\-[0-9]{2}\-[0-9]{4}$', data_nascimento):
        break
        else:
        print('Data de nascimento inválida')
    return data_nascimento


def validar_endereco():
    #valida o endereço do usuário
    while True:
        endereco = input(
            'Informe o seu endereço (logradouro,numero-bairro-cidade/Sigla: ')
        if re.search(
            r'^[A-Z][\w\s\-\.]+\,[\s?0-9]+\-[\w\s\-\.]+\-[\w\s\-\.]+\/[A-Z]{2}$',
            endereco):
        print('Endereço válido')
        else:
        print("Endereço inválido")
        return endereco


def validar_nome():
    #validia o nome do usuário
    while True:
        nome = input('Informe o seu nome completo: ')
        if re.search(r'^[A-Z][a-z]+\s[A-Z][a-z]+$', nome):
        break
        else:
        print('Nome inválido')
    return nome


def validar_usuario(usuarios, cpf):
    #valida se o usuário está cadastrado
    checar_usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return checar_usuario[0] if checar_usuario else None


def criar_conta(agencia, numero_conta, usuarios):
    #cria a conta do usuário corrente para o usuário
    cpf = input('Digite o CPF: ')
    usuario = validar_usuario(usuarios, cpf)
    if usuario:
        print('Conta criada com sucesso.')
        return {'agencia': agencia, 'conta': numero_conta, 'usuario': usuario}
    print('Usuário não encontrado, falha ao criar conta-corrente.')


def exibir_contas(contas):
    #Exibe as contas cadastradas
    print('----------CONTAS CADASTRADAS----------')
    for conta in contas:
        print(f'''\tAgência: \t{conta["agencia"]}
        Conta: \t\t{conta["conta"]}
        Usuário: \t{conta["usuario"]["nome"]}''')
        print('--------------------------------------')


extrato = ""
saldo = 0
usuarios = []
AGENCIA = '0001'
numero_conta = 1
contas = []
contador = 1
limite = 500
LIMITE_SAQUES = 3
numero_saques = 0

while True:
    #executa o loop para seleção dos itens no menu
    opcao = int(input(menu))
    if opcao == 0:
        print('Encerrando operação.')
        break

    elif opcao == 1:
        checar_extrato(saldo, extrato=extrato)

    elif opcao == 2:
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == 3:
        saldo, extrato, numero_saques = saque(saldo=saldo,extrato=extrato,limite=limite,LIMITE_SAQUES=LIMITE_SAQUES,numero_saques=numero_saques)

    elif opcao == 4:
        criar_usuario(usuarios)

    elif opcao == 5:
        numero_conta = contador
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        contador += 1
        if conta:
        contas.append(conta)
    elif opcao == 6:
        exibir_contas(contas)
    else:
        print('Opção inválida.')
