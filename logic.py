def gameLogic(randomWord, wordTyped):
    dictLetter = {'0': '', '1': '', '2': '', '3': '', '4': ''}
    index_finish = 0
    win = 0

    def addDict(index, color):
        if index == 0:
            dictLetter['0'] = color
        elif index == 1:
            dictLetter['1'] = color
        elif index == 2:
            dictLetter['2'] = color
        elif index == 3:
            dictLetter['3'] = color
        elif index == 4:
            dictLetter['4'] = color

    def lettersCounter(letterTyped):
        letters_quantity = 0
        
        for letters in randomWord:
            if letters == letterTyped: letters_quantity += 1 
        return letters_quantity
    
    letters_check = list()
    indexList = []

    # Função para identifica os verdes antes dos amarelos
    def green_check(index, letter):
        for indexRandom, letterRandom in enumerate(randomWord):
            if indexRandom == index and letterRandom == letter:
                addDict(index, 'green')
                indexList.append(index)
                letters_check.append(letter)
                return True
    
    # Função chamada para identificar os amarelos depois dos verdes
    def yellow_check(index, letter):
        quantity_total = lettersCounter(letter)
        quantity_check = 0
        indexStr = ''

        for i in indexList: indexStr += str(i)
        for check in letters_check:
            if check == letter: quantity_check += 1

        if quantity_total - quantity_check != 0 and str(index) not in indexStr:
            addDict(index, 'yellow')
            letters_check.append(letter)
        elif str(index) not in indexStr: addDict(index, 'grey')

    def checkLetters():
        # Verificar verdes e letras únicas
        for indexTyped, letterTyped in enumerate(wordTyped):
            if letterTyped in randomWord:
                quantity_letters = lettersCounter(letterTyped)
                if quantity_letters == 1:
                    if letterTyped not in letters_check:
                        green_check(indexTyped, letterTyped)
                    else:
                        addDict(indexTyped, 'grey')
                else:
                    green_check(indexTyped, letterTyped)
            else:
                addDict(indexTyped, 'grey')
        
        # Verificar amarelos
        for indexTyped, letterTyped in enumerate(wordTyped):
            if letterTyped in randomWord:
                yellow_check(indexTyped, letterTyped)
                
    checkLetters()
    
    # Input das letras com as cores
    for dictValue in dictLetter.values():
        if dictValue == 'green':
            print(f'\033[32m{wordTyped[index_finish]}\033[0m', end=' ')
            index_finish += 1
        elif dictValue == 'yellow':
            print(f'\033[33m{wordTyped[index_finish]}\033[0m', end=' ')
            index_finish += 1
        elif dictValue == 'grey':
            print(f'\033[90m{wordTyped[index_finish]}\033[0m', end=' ')
            index_finish += 1

    for value_dict in dictLetter.values():
        if value_dict == 'green': win += 1

    if win == 5:
        return 'Win'
    else:
        return 'Lose'