import random  # Importa o módulo random para gerar números aleatórios

# Função para exibir a mensagem de abertura do jogo
def mensagen_de_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

# Função para exibir a mensagem de seleção de nível de dificuldade e retornar o total de tentativas
def mensagen_de_nivel():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    # Define o número de tentativas com base no nível escolhido
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    return total_de_tentativas

# Função principal do jogo
def jogar():
    mensagen_de_abertura()

    numero_secreto = random.randrange(1, 101)  # Gera um número secreto aleatório entre 1 e 100
    pontos = 1000  # Define a pontuação inicial do jogador

    total_de_tentativas = mensagen_de_nivel()  # Obtém o número de tentativas com base no nível

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        # Verifica se o chute está dentro do intervalo permitido
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos - 50

    print("Fim do jogo")

if __name__ == "__main__":
    jogar()  # Inicia o jogo quando o script é executado