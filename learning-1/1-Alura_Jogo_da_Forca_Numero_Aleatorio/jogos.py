import forca  # Importa o módulo do jogo da Forca
import adivinhacao  # Importa o módulo do jogo de Adivinhação

# Função para permitir que o jogador escolha entre os jogos disponíveis
def escolhe_jogo():
    print("*********************************")
    print("******* Escolha o seu jogo! *******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))  # Solicita ao jogador que escolha um jogo

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()  # Inicia o jogo da Forca chamando a função jogar() do módulo forca
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()  # Inicia o jogo de Adivinhação chamando a função jogar() do módulo adivinhacao

if __name__ == "__main__":
    escolhe_jogo()  # Inicia a função de escolha de jogo quando o script é executado