def gameLogic(randomWord, wordTyped):
    dictLetter = {'0': '', '1': '', '2': '', '3': '', '4': ''}

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

    def green_check(index, letter):
        # Identifica os verdes
        for indexRandom, letterRandom in enumerate(randomWord):
            if indexRandom == index and letterRandom == letter:
                addDict(index, 'green')
                indexList.append(index)
                letters_check.append(letter)
                return True
            
        return False
    
    def yellow_check(index, letter):
        # Identifica os amarelos depois dos verdes
        quantity_total = lettersCounter(letter)
        quantity_check = 0
        indexStr = ''

        for i in indexList: indexStr += str(i)

        for check in letters_check:
            if check == letter: quantity_check += 1

        if quantity_total - quantity_check != 0 and str(index) not in indexStr:
            addDict(index, 'yellow')
            letters_check.append(letter)
        elif str(index) not in indexStr:
            addDict(index, 'grey')

    def checkLetters():
        # Verificar verdes e letras únicas
        for indexTyped, letterTyped in enumerate(wordTyped):
            if letterTyped in randomWord:
                quantity_letters = lettersCounter(letterTyped)
                if quantity_letters == 1:
                    if letterTyped not in letters_check:
                        result = green_check(indexTyped, letterTyped)
                        if result == False:
                            addDict(indexTyped, 'grey')
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
    print(dictLetter)
    win = 0

    for value_dict in dictLetter.values():
        if value_dict == 'green': win += 1

    if win == 5:
        return 'Win'
    else:
        return 'Lose'
    
    # False = Amarelo
    # True = Verde
    # None = Cinza
    
