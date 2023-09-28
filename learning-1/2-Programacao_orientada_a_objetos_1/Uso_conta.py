from Conta import Conta  # Importa a classe Conta do arquivo Conta.py

def main():
    # Criando uma instância da classe Conta
    minha_conta = Conta("12345-6", "João", 1000.0, 2000.0)

    # Realizando operações na conta
    minha_conta.deposita(500.0)
    minha_conta.saca(200.0)

    # Exibindo informações da conta
    minha_conta.extrato()
    print("Saldo: R$ {}".format(minha_conta.saldo))
    print("Titular: {}".format(minha_conta.get_titular))
    print("Limite de saque: R$ {}".format(minha_conta.limite))

if __name__ == "__main__":
    main()  # Chama a função main() ao executar main.py diretamente