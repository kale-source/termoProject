def gameLogic(randomWord, wordTyped):
    win = 0
    letters_check = []
    
    # Faz a contagem da letra existente no randomWord
    def checkLetters(typedLetter):
        countTotal = 0
        for countRandom in randomWord:
            if countRandom == typedLetter: countTotal += 1
        if typedLetter not in letters_check:
            letters_check.append(typedLetter)
            return True
        else:
            check_quantity = 0
            for check in letters_check:
                if check == typedLetter: check_quantity += 1
            if check_quantity < countTotal:
                letters_check.append(typedLetter)
                return True
            else:
                return False

    # Função para comparar a palavra digitada pelo usuário com a palavra sorteada e a posição
    def checkPosition(indexTyped, letterTyped):
        for indexRandom, randomTyped in enumerate(randomWord):
            if letterTyped == randomTyped and indexRandom == indexTyped:
                return True # Tem a letra e está na posição correta e retorna true
        return False # Retorna False ou seja, tem na palavra, mas está na posição errada

    # For para palavra digitada pelo usuário
    for index, typed in enumerate(wordTyped):
        if typed in randomWord:
            checkResult = checkLetters(typed)
            result = checkPosition(index, typed)
            if checkResult == True:
                if result == False:
                    print(f'{'\033[93m'}{typed}{'\033[0m'}', end=' ') # Retorna amarelo
                else:
                    win += 1
                    print(f'{"\033[32m"}{typed}{'\033[0m'}', end=' ') # Retorna verde
            else:
                print(f'{'\033[90m'}{typed}{'\033[0m'}', end=' ')
        else:
            print(f'{'\033[90m'}{typed}{'\033[0m'}', end=' ') # Retorna cinza

    if win == 5:
        return 'Win'
    else:
        return 'Lose'
    
    # False = Amarelo
    # True = Verde
    # None = Cinza
    
