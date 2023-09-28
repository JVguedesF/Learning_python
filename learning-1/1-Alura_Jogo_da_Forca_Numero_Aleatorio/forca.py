import random  # Importa o módulo random para gerar palavras aleatórios

# Função para exibir a mensagem de abertura do jogo
def mensagen_de_abertura():
    print("***********************************")
    print("*** Bem vindo ao jogo da Forca! ***")
    print("***********************************")
    print("***********É uma Fruta*************")

# Função para obter uma palavra secreta aleatória do arquivo "_Frutas.txt"
def a_palavra_secreta():
    arquivo = open("_Frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

# Função para pedir ao jogador que escolha uma letra
def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

# Função para marcar letras corretas no jogo
def marcador_de_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def mensagen_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    # Chama a função de abertura do jogo para exibir uma mensagem de boas-vindas
    mensagen_de_abertura()

    # Obtém uma palavra secreta aleatória do arquivo "_Frutas.txt"
    palavra_secreta = a_palavra_secreta()

    # Inicializa uma lista com underscores representando letras a adivinhar
    letras_acertadas = ["_" for _ in palavra_secreta]

    # Inicializa variáveis para controlar se o jogador ganhou, perdeu e quantos erros cometeu
    enforcou = False
    acertou = False
    erros = 0

    # Exibe as letras adivinhadas até o momento na forma de underscores
    print(letras_acertadas)

    # Entra em um loop que continua até que o jogador acerte todas as letras ou exceda o limite de erros
    while not enforcou and not acertou:

        # Solicita ao jogador que insira uma letra
        chute = pede_chute()

        # Verifica se a letra inserida está na palavra secreta e atualiza a lista de letras acertadas
        if chute in palavra_secreta:
            marcador_de_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            # Se a letra não estiver na palavra secreta, incrementa o contador de erros e desenha a forca
            erros += 1
            desenha_forca(erros)

        # Verifica se o jogador excedeu o limite de erros (6) ou acertou todas as letras
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        # Exibe as letras adivinhadas até o momento
        print(letras_acertadas)

    # Se o jogador acertou todas as letras, exibe uma mensagem de vitória
    if acertou:
        mensagen_ganhou()
    else:
        # Se o jogador excedeu o limite de erros, exibe uma mensagem de derrota
        imprime_mensagem_perdedor(palavra_secreta)

if __name__ == "__main__":
    jogar()  # Inicia o jogo quando o script é executado
