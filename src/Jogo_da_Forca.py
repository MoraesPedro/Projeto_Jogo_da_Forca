# Imports libs

import unicodedata    

# Funcoes 

def desenhaForcamMensagem():
    print()
    print('   +------------+ ')  
    print('   |  /         | ')
    print('   | /         _|_ ')
    print('   |/         |. .|')
    print('   |          |_x_|  ___ Se mudarem de idéia e quiserem jogar, é só rodar o algoritimo de novo ___')
    print('   |          __|__ ')
    print('   |        /|     |\\')
    print('   |       / |     | \\')
    print('   |      /  |_____|  \\')
    print('   |          |_|_|')
    print('   |          /   \\')
    print('   |         /     \\')
    print('   |        /       \\')
    print('   |   ')
    print('-------')
    
    
# Jogo Completo

def jogo_forca():

    vidasGastas = 0
    palavraMagica = ''
    palavraForca = '_'  # palavra que vai aparecer sempre pro usuario
    letrasChutadas = []
    letrasCorretas = []
    pedeLetra = ''

    validacaoInicio = input('Hello, jogadores!\n\nBem vindos ao Jogo da Forca\n\n\nDigite ***iniciar*** para rodar o jogo: \n\n').upper().strip()

    if validacaoInicio == 'INICIAR':
        print('\n\n\nCuidado com a forca e divirta-se!\n\n')
        
        palavraUsuario = input('Digite aqui a palavra chave para a forca: ')
        palavraMagica = list(unicodedata.normalize("NFD", palavraUsuario).encode("ascii", "ignore").decode("utf-8").upper().strip())
        palavraMagicaCopy = palavraMagica.copy()
        palavraForca = list('_' * len(palavraMagica))
        
        # proximo for esconde a palavra digitada
        
        for escondepalavraMagica in range(33):
            print('\t\txxxxxxxxxxxxxxxxxxx')
            print('\t\txx Hello, World! xx')
            print('\t\txxxxxxxxxxxxxxxxxxx')
            

        print()
        print('*** Regras do jogo da Forca ***\n')
        print('1. O jogador tem um total de 6 vidas.')
        print('2. Chuta-se uma letra por vez.')
        print('3. Pode chutar uma palavra por vez.')
        print('4. Ç será o mesmo que C e os acentos não serão representados, serão letras normais.\n')
        print('\nShow!\n\nA palavra escolhida tem um total de', len(palavraMagica), 'letras!\n')
        print()

        #comeco do chuta letra
        
        while palavraForca != palavraMagica:
            
            pedeLetra = input('Digite aqui uma letra ou a palavra: ').upper()
            if len(pedeLetra) > 1 and len(pedeLetra) != len(palavraMagica):
                print('\n\n*Entrada inválida*\n\n- Só é possível chutar uma letra por vez ou palavas de mesmo tamanho!\n\n')
                vidasGastas -=1

            for el in palavraMagicaCopy:
                if el == pedeLetra:
                    palavraForca[palavraMagicaCopy.index(pedeLetra)] = el
                    if palavraMagicaCopy.count(pedeLetra) > 1:
                        palavraMagicaCopy[palavraMagicaCopy.index(pedeLetra)] = '_'
            
            if list(pedeLetra) == palavraMagica:
                print('\n\n\nParabés Jogador, você conseguiu acertar a palavra da forca - ' + ''.join(palavraMagica).capitalize() + '!\n')
                print(''.join(palavraMagica).capitalize())
                break

            #pedeLetra = input('Digite aqui uma letra: ').upper()

            if pedeLetra in letrasChutadas:
                print('\nEntrada inválida - Letra já foi chutada\n')
                continue #ver com alguém depois eu do futuro se 

            else:
                letrasChutadas.append(pedeLetra) # se nao estiver aqui o if nao funciona pq letrasChutadas tem que ficar vazia

                if pedeLetra in palavraMagica:
                    letrasCorretas.append(pedeLetra)

                else:
                    vidasGastas += 1
            
            
            if vidasGastas == 0:
                print()
                print('   +------------+ ')  
                print('   |  /         | ')
                print('   | / ')
                print('   |/ ')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('-------')
            elif vidasGastas == 1:
                print()
                print('   +------------+ ')  
                print('   |  /         | ')
                print('   | /         _|_ ')
                print('   |/         |. .|')
                print('   |          |_x_|')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('-------')
        
            elif vidasGastas == 2:
                print()
                print('   +------------+ ')  
                print('   |  /         | ')
                print('   | /         _|_ ')
                print('   |/         |. .|')
                print('   |          |_x_|')
                print('   |          __|__ ')
                print('   |         |     |')
                print('   |         |     |')
                print('   |         |_____|')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('-------')
            elif vidasGastas == 3:
                print()
                print('   +------------+ ')  
                print('   |  /         | ')
                print('   | /         _|_ ')
                print('   |/         |. .|')
                print('   |          |_x_|')
                print('   |          __|__')
                print('   |         |     |\\')
                print('   |         |     | \\')
                print('   |         |_____|  \\')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |   ')
                print('-------')
            elif vidasGastas == 4:
                print()
                print('   +------------+ ')  
                print('   |  /         | ')
                print('   | /         _|_ ')
                print('   |/         |. .|')
                print('   |          |_x_|')
                print('   |          __|__')
                print('   |        /|     |\\')
                print('   |       / |     | \\')
                print('   |      /  |_____|  \\')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |   ')
                print('-------')
            elif vidasGastas == 5:
                print()
                print('   +------------+ ')  
                print('   |  /         | ')
                print('   | /         _|_ ')
                print('   |/         |. .|')
                print('   |          |_x_|')
                print('   |          __|__ ')
                print('   |        /|     |\\')
                print('   |       / |     | \\')
                print('   |      /  |_____|  \\')
                print('   |            |_|')
                print('   |              \\')
                print('   |               \\')
                print('   |                \\')
                print('   |   ')
                print('-------')
            else:
                print()
                print('   +------------+ ')  
                print('   |  /         | ')
                print('   | /         _|_ ')
                print('   |/         |x x|')
                print('   |          |_x_|')
                print('   |          __|__ ')
                print('   |        /|     |\\')
                print('   |       / |     | \\')
                print('   |      /  |_____|  \\')
                print('   |          |_|_|')
                print('   |          /   \\')
                print('   |         /     \\')
                print('   |        /       \\')
                print('   |   ')
                print('-------')
                print()
                print('\nVocê morreu!\n')
                break
            print(''.join(palavraForca) + '\n')
        
            if palavraForca == palavraMagica :
                ('Parabés Jogador, você conseguiu acertar a palavra!\n')
                break
            
        
        if vidasGastas == 6 :
            print('\n\n***Fim de jogo***\n\nObrigado por jogar!\n')

        elif palavraMagica == palavraForca or list(pedeLetra) == palavraMagica:
            print('\nVocê ganhou!\n\nFim de jogo\n\nObrigado por jogar!\n')
        
        jogar_novamente = input('n\nJogar novamente?\n\n\nDigite ***Sim/Não***\n\n').upper().strip()

        if jogar_novamente == 'SIM' or jogar_novamente == 'S':
            jogo_forca()
        else:
            print('\nAté logo!\n')

    else:
        desenhaForcamMensagem()
        return



jogo_forca()  