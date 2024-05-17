menu = """---------------------
MENU
[1] EXTRATO
[2] DEPÓSITO
[3] SAQUE
[4] USUÁRIO
[5] CONTA-CORRENTE
[0] SAIR
---------------------
"""

#usuarios = cadastrar_usuario()]


def verificar_extrato(saldo,/,*,extrato):
  print("------------EXTRATO------------")
  print(extrato if extrato else "Nenhuma movimentação realizada")
  print(f"\nSaldo: R${saldo:.2f}")
  print("-------------------------------")

def depositar(saldo, extrato,valor,/):
  valor=float(input("Informe o valor do depósito: "))
  if valor <= 0:
    print("Valor inválido")
    return
  saldo+=valor
  extrato+=f"Depósito: R$ {valor:.2f}\n"
  print("Depósito realizado com sucesso!")
  return saldo, extrato

def sacar(*,saldo, valor, extrato, numero_saques, limite, LIMITE_SAQUES):
  valor=float(input("Informe o valor do saque: "))
  if valor <= 0:
    print("Valor inválido")
  elif valor > saldo:
    print("Saldo insuficiente")
  elif numero_saques >= LIMITE_SAQUES:
    print("Número máximo de saques atingido")
  elif valor > limite:
    print("Limite diário de saque atingido")
  else:
    saldo-=valor
    extrato+=f"Saque: R$ {valor:.2f}\n"
    numero_saques+=1
    print("Saque realizado com sucesso!")

  return saldo, extrato, numero_saques

def cadastrar_usuario(usuarios):
  cpf = input("Informe o seu CPF(Somente números): ")
  usuario = validar_usuarios(usuarios, cpf)
  if usuario:
    print("Usuário já cadastrado")
    return

  nome = input("Informe o seu nome: ")
  data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
  endereco = input(
      "Informe o seu endereço (Logradouro, numero-bairro-cidade/sigla do Estado): "
  )

  usuarios.append({
      "nome": nome,
      "cpf": cpf,
      "data_nascimento": data_nascimento,
      "endereco": endereco
  })
  print("Usuário cadastrado com sucesso!")
  return cpf

def validar_usuarios(usuarios, cpf):
  checar_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return checar_usuario[0] if checar_usuario else None


def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário:")
  usuario= validar_usuarios(usuarios, cpf)
  if usuario:
    print("Conta criada com sucesso!"  )
    return{"agencia":agencia,"numero_conta": numero_conta, "usuario": usuario}

  print("Usuário não encontrado, encerrando operação de criação de conta")




# Programa Principal
AGENCIA ="0001"
numero_conta = 0
extrato = ""
saldo =0
limite = 500
LIMITE_SAQUES = 3
numero_saques=0
usuarios = []
contas = []
valor = 0
contador = 1

while True:
  opcao=int(input(menu))
  if opcao == 1:
    verificar_extrato(saldo, extrato=extrato)
  elif opcao == 2:
    saldo,extrato = depositar(saldo, extrato,valor)
  elif opcao == 3:
    saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)
  elif opcao == 4:
    cadastrar_usuario(usuarios)
  elif opcao == 5:
    numero_conta = contador
    conta = criar_conta(AGENCIA, numero_conta, usuarios)
    contador+=1

    if conta:
      contas.append(conta)

  else:
    print("Encerrando operações.")
    break

