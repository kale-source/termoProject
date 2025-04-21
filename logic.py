def gameLogic(randomWord, wordTyped):
    win = 0
    # Faz a contagem da letra existente no randomWord
    def quantityLetters(typedLetter):
        countTotal = 0
        for count in wordTyped:
            if count == typedLetter: countTotal += 1
        return countTotal

    # Função para comparar a palavra digitada pelo usuário com a palavra sorteada e a posição
    def checkPosition(indexTyped, letterTyped):
        for index, random in enumerate(randomWord):
            if letterTyped == random and index == indexTyped:
                return True
        return False

    # For para palavra digitada pelo usuário
    for index, typed in enumerate(wordTyped):
        if typed in randomWord:
            quantityLetters(typed)
            result = checkPosition(index, typed)
            if result == False:
                quantity = quantityLetters(typed)
                if quantity != 1:
                    print(f'{'\033[90m'}{typed}{'\033[0m'}', end=' ')
                else:
                    print(f'{'\033[93m'}{typed}{'\033[0m'}', end=' ')
            else:
                win += 1
                print(f'{"\033[32m"}{typed}{'\033[0m'}', end=' ')
        else:
            print(f'{'\033[90m'}{typed}{'\033[0m'}', end=' ')

    if win == 5:
        return 'Win'
    else:
        return 'Lose'
    # False = Amarelo
    # True = Verde
    # None = Cinza
    
