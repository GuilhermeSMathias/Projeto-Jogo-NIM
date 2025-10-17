def computador_escolhe_jogada(n: int, m: int) -> int:
    """
    Lógica do computador para escolher a melhor jogada com base na estratégia m+1

    Args:
        - n (int): número atual de peças no tabuleiro
        - m (int): número máximo de peças a ser removida na jogada

    Returns:
        - (int): número de peças a ser retirada pelo computador
    """
    for i in range(1, m):
        if (n - i) % (m + 1) == 0:
            return i
    return m


def iniciar():
    """
    Dá a tela de opções e inicia o jogo.

    Returns: None
    """
    global contra_pessoa
    
    print(f"""
    {'| Jogo do Nim |':=^60}
    """)

    mostrar_opcoes()

    while True:
        op = str(input('Digite número da opção desejada: '))
        match op:
            case '1':
                contra_pessoa = True
                partida()
                break
            case '2':
                contra_pessoa = True
                campeonato()
                break
            case '3':
                contra_pessoa = False
                partida()
                break
            case '4':
                contra_pessoa = False
                campeonato()
                break
            case '5':
                break
            case _:
                print('Opção inválida. Tente novamente.')

def mostrar_opcoes():
    print("""
    Selecione o modo de jogo:
    1 - Jogar uma partida (Jogador x Jogador)
    2 - Jogar um campeonato (Jogador x Jogador)
    3 - Jogar uma partida (Jogador x Máquina)
    4 - Jogar um campeonato (Jogador x Máquina)
    5 - Fechar programa
    """)
    

def partida():
    global contra_pessoa
    print('Partida')
    print(contra_pessoa)

def campeonato():
    global contra_pessoa
    print('Campeonato')
    print(contra_pessoa)
    
iniciar()
