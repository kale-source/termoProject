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
            tWords = str(input(f'{gameRound} - Digite a palavra: ')).strip()
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