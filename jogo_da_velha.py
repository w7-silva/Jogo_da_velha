tabuleiro = [" "] * 9

# Função a qual exibe o tabuleiro de forma visual
def exibir_tabuleiro():
    print()
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
    print()

# Função para verificar se um jogador venceu
def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinacao in combinacoes_vencedoras:
        if all(tabuleiro[i] == jogador for i in combinacao):
            return True
    return False

# Função que verifica o empate
def verificar_empate(tabuleiro):
    return " " not in tabuleiro

# Função Minimax. Inteligência da máquina
def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vencedor(tabuleiro, "X"):
        return -10 + profundidade # Derrota da máquina
    if verificar_vencedor(tabuleiro, "O"):
        return 10 - profundidade # Vitória da máquina
    if verificar_empate(tabuleiro):
        return 0
    
    if maximizando:
        melhor_valor = -float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                valor = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = " "
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "X"
                valor = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = " "
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# Função para escolher a melhor jogada da máquina    
def melhor_jogada(tabuleiro):
    melhor_valor = -float("inf")
    melhor_posicao = -1

    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = " "
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i
    return melhor_posicao

# Essa é a função principal do jogo
def jogar_jogo():
    while True:
        exibir_tabuleiro()

        # Turno do jogador X
        while True:
            try:
                jogada = int(input("Escolha sua posição (0-8): "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":
                    break
                else:
                    print("Posição inválida. Tente novamente!")
            except ValueError:
                print("Digite um número entre 0 a 8.")
        
        tabuleiro[jogada] = "X"

        if verificar_vencedor(tabuleiro, "X"):
            exibir_tabuleiro()
            print("The best! Você venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Opa, opa. Essa deu empate!")
            break

        print("Computador está pensando...")
        melhor_posicao = melhor_jogada(tabuleiro)
        tabuleiro[melhor_posicao] = "O"

        if verificar_vencedor(tabuleiro, "O"):
            exibir_tabuleiro()
            print("Dessa vez não deu, o computador venceu.")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Opa, opa. Essa deu empate!")
            break

# Início da execução do programa
print("""
 ______________________________________      
|     Bem vindo ao 'JOGO DA VELHA'!    |
|--------------------------------------|
|As posições são numeradas dessa forma:|           
|______________________________________|

0 | 1 | 2
--+---+--
3 | 4 | 5
--+---+--
6 | 7 | 8 """)

jogar_jogo()