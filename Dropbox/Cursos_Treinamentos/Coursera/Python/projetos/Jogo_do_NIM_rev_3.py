# Subprogramas

# n --> Número de peças inicialmente dispostas numa mesa ou tabuleiro.
# m --> Número máximo de peças que um jogador pode retirar em cada jogada.
computador = 0
usuario = 0
rodada = 0

def computador_escolhe_jogada(n, m):
    global computador
    n = n - m
    if (n == 1):
        print(" ")
        print("O computador tirou %s peça." % n)
        print("Agora restam %s peças no tabuleiro." % n)
        print(" ")
        if (n == 0):
            print ("Fim do jogo! O computador ganhou!")
            partida()
    else:
        print(" ")
        print("O computador tirou %s peça." % m)
        print("Agora restam %s peças no tabuleiro." % n)
        print(" ")
        if (n == 0):
            print ("Fim do jogo! O computador ganhou!")
            partida()
    return n
    return m


def usuario_escolhe_jogada(n, m):
    global usuario
    print(" ")
    n_user = int(input("Quantas peças você vai tirar? "))
    if (n_user <= m):
        n = n - m
        print(" ")
        print("Voce tirou %s peças." % n_user)
        print("Agora restam apenas %s peças no tabuleiro." % n)
    else:
        while (n_user > m):
            print(" ")
            print("Oops! Jogada inválida! Tente de novo.")
            print(" ")
            n_user = int(input("Quantas peças você vai tirar? "))
            print("Voce tirou %s peças." % n_user)
            print("Agora restam apenas %s peças no tabuleiro." % n)
    if (n == 0):
        print ("Vitoria do usuario")
    return n_user
    return n
    return m

def partida():
    global computador
    global usuario
    global rodada

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (((n )%(m + 1)) == 0):
        print(" ")
        print("Voce começa!")
        while (n > 0):
            usuario_escolhe_jogada(n,m)
            if (n>0):
                computador_escolhe_jogada(n,m)
    else:
        print(" ")
        print("Computador Começa!!")
        while( n > 0):
            computador_escolhe_jogada(n,m)
            if n > 0:
                usuario_escolhe_jogada(n,m)

# Programa Principal

print("Bem-vindo ao jogo do NIM! Escolha:")
print(" ")
print("1 - para jogar uma partida isolada ")
print("2 - para jogar um campeonato ")
tipo_jogo = int(input("Digite o número do seu tipo de jogo: "))
print(" ")
if ( tipo_jogo == 1 ):
    print("Voce escolheu partida isolada!")
    partida()
if ( tipo_jogo == 2):
    print("Voce escolheu um campeonato!")
    partida()
else:
    pass

""" As funções usuario_escolhe_jogada e computador_escolhe_jogada não estão retornando os valores contando o numero de peças
 tirados, preciso corrigir para que os valores das peças tiradas sejam contabilizadas na função partida."""