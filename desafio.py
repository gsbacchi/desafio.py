def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))
    usuario_existente = any(u["cpf"] == cpf for u in usuarios)
    if usuario_existente:
        print("Erro: já existe um usuário com esse CPF.")
        return
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (Rua, número - bairro - cidade/UF): ").strip()
    novo_usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso.")

def criar_conta_corrente(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("Erro: usuário não encontrado.")
        return
    numero_conta = len(contas) + 1
    conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario}
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso para {usuario['nome']}.")

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        criar_conta_corrente(contas, usuarios)

    elif opcao == "q":
        print("======= Agradecemos a sua fidelidade e preferência! =======")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
