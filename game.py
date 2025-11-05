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
            return n - i
    return n - m


def iniciar() -> None:
    """
    Mostra a tela de opções e inicia o jogo.

    Returns: None
    """
    global eh_contra_pessoa
    global eh_campeonato
    
    print(f"{'| Jogo do Nim |':=^80}")

    print("""Selecione o modo de jogo:\n1 - Jogar uma partida (Jogador x Jogador)\
    \n2 - Jogar um campeonato (Jogador x Jogador)\n3 - Jogar uma partida (Jogador x Máquina)\
    \n4 - Jogar um campeonato (Jogador x Máquina)\n5 - Fechar programa
    """)

    while True:
        op = str(input('Digite número da opção desejada: '))
        match op:
            case '1':
                eh_contra_pessoa = True
                eh_campeonato = False
                partida()
                break
            case '2':
                eh_contra_pessoa = True
                eh_campeonato = True
                campeonato()
                break
            case '3':
                eh_contra_pessoa = False
                eh_campeonato = False
                partida()
                break
            case '4':
                eh_contra_pessoa = False
                eh_campeonato = True
                campeonato()
                break
            case '5':
                print('Adeus!')
                break
            case _:
                print('Opção inválida. Tente novamente.')

    
def partida(jogador_1: str='', jogador_2: str='') -> None:
    """
    Inicia a partida

    Args:
        - jogador_1 (str): nome do jogador 1
        - jogador_2 (str): nome do jogador 2

    Returns:
        - (str): nome do jogador vencedor da partida
    """
    global eh_contra_pessoa
    global eh_campeonato
    
    print(f"{'| Configuração da Partida |':=^80}")

    # Definindo estilo de jogo
    if eh_contra_pessoa:
        if not eh_campeonato:
            jogador_1 = str(input('Digite o nome do 1º jogador: ')).strip().capitalize()
            jogador_2 = str(input('Digite o nome do 2º jogador: ')).strip().capitalize()

        n, m = definir_tabuleiro()

        mostrar_tabuleiro(n, m)

        # Definindo ordem
        while True:
            ordem = str(input(f'{jogador_1} joga primeiro? [S/N] ')).strip().upper()

            if ordem != 'S' and ordem != 'N':
                print('Inválido. Responda S ou N.')
                continue
            else:
                break

        s = True if ordem == 'S' else False

        # Game loop  
        while n != 0:
            print(f'Jogada de {jogador_1}' * s, end='')
            print(f'Jogada de {jogador_2}' * (not s))

            n = usuario_escolhe_jogada(n, m)
            mostrar_tabuleiro(n, m)

            # Condição de parada
            if n == 0:
                if s:
                    print(f'{jogador_1} ganhou!')
                    return jogador_1
                else:
                    print(f'{jogador_2} ganhou!')
                    return jogador_2
            else:
                # Alterna jogador
                s = not s

    else:
        n, m = definir_tabuleiro()

        mostrar_tabuleiro(n, m)

        # Definindo ordem        
        if n % (m + 1) == 0:
            print('Você começa!')
            s = True
        else:
            print('Computador começa!')
            s = False

        # Game loop  
        while n != 0:
            if s:
                print('Vez do jogador')
                n = usuario_escolhe_jogada(n, m)
            else:
                print('Vez do computador')
                n_antes = n
                n = computador_escolhe_jogada(n, m)
                print(f'O computador removeu {n_antes - n} peças do tabuleiro')

            mostrar_tabuleiro(n, m)

            # Condição de parada
            if n == 0:
                if s:
                    print('Jogador venceu!')
                    return 'Jogador'
                else:
                    print('Computador venceu!')
                    return 'Computador'
            else:
                # Alterna entre jogador e computador
                s = not s
            


def definir_tabuleiro() -> tuple:
    """
    Define a configuração do tabuleiro, com o número de peças dispostas e o número máximo de peças que podem ser retiradas por turno

    Returns:
        - (tuple): valor de peças do tabuleiro e valor máximo de peças retiradas (n, m)
    """
    while True:
        try:
            while (n := int(input('Digite número de peças no tabuleiro: '))) <= 0:
                print('Valor inválido. Tente novamente.')

            while (m := int(input('Digite número máximo de peças que podem ser tiradas por turno: '))) <= 0 or m > n:
                print('Valor inválido. Tente novamente.')
                
            return n, m

        except ValueError:
            print('Valor inválido. Tente novamente.')

def mostrar_tabuleiro(n: int, m: int) -> None:
    """
    Mostra o estado atual do tabuleiro com base nos parâmetros passados

    Args:
        - n (int): número atual de peças no tabuleiro
        - m (int): número máximo de peças a ser removida na jogada

    Returns: None
    """
    print(f"{'| Tabuleiro |':=^80}")
    print(' (#) ' * n)
            
def campeonato() -> None:
    """
    Inicia o campeonato

    Returns: None
    """
    global eh_contra_pessoa
    global eh_campeonato


    if eh_contra_pessoa:
        jogador_1 = str(input('Digite o nome do 1º jogador: ')).strip().capitalize()
        jogador_2 = str(input('Digite o nome do 2º jogador: ')).strip().capitalize()

        p_jogador_1 = 0
        p_jogador_2 = 0
        
        for p in range(1, 4):
            print(f"{'| ' + str(p) + 'º Partida |':=^80}")
            vencedor = partida(jogador_1, jogador_2)
            if vencedor == jogador_1:
                p_jogador_1 += 1
            else:
                p_jogador_2 += 1

        placar_jogador(jogador_1, jogador_2, p_jogador_1, p_jogador_2)
        
    else:
        p_jogador = 0
        p_computador = 0

        for p in range(1, 4):
            print(f"{'| ' + str(p) + 'º Partida |':=^80}")
            vencedor = partida()
            if vencedor == 'Jogador':
                p_jogador += 1
            else:
                p_computador += 1

        print()
        print(f"""Placar final\nJogador: {p_jogador}\nComputador: {p_computador}""")
        if p_jogador > p_computador:
            print('Jogador ganhou!')
        else:
            print('Computador ganhou!')
            
        
def usuario_escolhe_jogada(n: int, m: int) -> int:
    """
    Função para usuário escolher jogada
    
    Args:
        - m (int): valor máximo que usuário pode escolher
        - n (int): o valor da quantidade de peças
    Return:
        - (int): o novo valor de quantidade peças após remoção
    """
    p = int(input('Qual o valor da sua jogada? '))
    
    while not (p <= m):
        print('Jogada inválida, tente novamente')
        p = int(input('Qual o valor da sua jogada? '))

    if n > p:
        n = n - p
        return n
    else:
        return 0

def placar_jogador(jogador_1: str, jogador_2: str, p_jogador_1 : int , p_jogador_2 : int) -> int:
    """
    Função para mostrar o placar quando é jogador versus jogador
    
    Args:
        - jogador_1 (str): variável referente aos pontos do jogador 1
        - jogador_2 (str): variável referente aos pontos do jogador 2
        - p_jogador_1 (int): variável referente aos pontos do jogador 1
        - p_jogador_2 (int): variável referente aos pontos do jogador 2

    Returns: None
    """
    print()
    print(f"""Placar final\n{jogador_1}: {p_jogador_1}\n{jogador_2}: {p_jogador_2}""")
    if p_jogador_1 > p_jogador_2:
        print(f'O jogador {jogador_1} ganhou!')
    else:
        print(f'O jogador {jogador_2} ganhou!')


iniciar()
