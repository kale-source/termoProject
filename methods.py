import random
from logic import gameLogic

class Methods:
    # Método para escolher uma palavra aleatória do dicionário  
    @staticmethod
    def sortedWord():
        words = []
        with open('words.txt', 'r', encoding='utf-8') as f:
            for linha in f: 
                if len(linha.strip()) == 5:
                    words.append(linha.rstrip('\n'))
        return random.choice(words)
    
    # Iniciar o jogo
    @staticmethod
    def gameStart(randomWord):
        gameRound = 1
        while gameRound <= 6:
            check_number_status = True
            tWords = str(input(f'{gameRound} - Digite a palavra: ')).strip()

            for check_number in tWords:
                if check_number in '0123456789':
                    print(f'A palavra que digitou tem números, digite novamente!')
                    check_number_status = False

            if check_number_status:
                if len(tWords) != 5:
                    print(f'A palavra que digitou tem {len(tWords)} caracteres, digite novamente!')
                else:
                    result = gameLogic(randomWord, tWords)
                    if result == 'Win':
                        print('', end='\n')
                        print('Parabéns, você venceu!')
                        break
                    elif gameRound == 6 and result == 'Lose':
                        print('', end='\n')
                        print('Poxa.. você perdeu, tente novamente!')
                        print(f'A palavra era {randomWord}!')

                    gameRound += 1
            print('', end='\n')