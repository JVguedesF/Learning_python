from Data import Data  # Importe a classe Data do arquivo Data.py

def main():
    # Criando uma instância da classe Data
    minha_data = Data(11, 9, 2023)

    # Chamando o método para imprimir a data formatada
    minha_data.formatada()  # Isso imprimirá "11/9/2023" no console

if __name__ == "__main__":
    main()  # Chama a função main() ao executar uso_data.py diretamente
