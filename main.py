from methods import Methods

try:
    while True:
        repeat_game = True
        wordSorted = Methods.sortedWord()
        Methods.gameStart(wordSorted)

        while True:
            try:
                finish_check = int(input('Digite [0] para encerrar o jogo\nDigite [1] para continuar uma nova rodada\n-> '))
                if finish_check != 0 and finish_check != 1:
                    print(f'{finish_check} não é uma opção válida!')
                elif finish_check == 0:
                    repeat_game = False
                    break
                else:
                    break
            except ValueError:
                print('Ops, aconteceu um erro, verifique se não inseriu um caractere fora de padrão.')

        if repeat_game == False: break
except ValueError:
    print('Ops, houve algum erro!')
