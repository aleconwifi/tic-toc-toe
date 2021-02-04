theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }


board_keys = []

for key in theBoard:
    board_keys.append(key)

print('Bienvenido al juego')


def board():
    print(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])
    print('-+-+-')
    print(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
    print('-+-+-')
    print(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])


turn = '❌'
count = 0


#si la casilla esta vacia, entonces la marco

while(count<=8):

    board()
    move = input("Es tu turno," + turn + " A cual lugar quieres mover?")
# Hola aqui valido los if

    if move.isnumeric():
        if 1 <= int(move) <=9:
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count=count+1
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                    board()
                    print(f'Ganaste {turn}')
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                    board()
                    print(f'Ganaste {turn}')
                    break 
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                    board()
                    print(f'Ganaste {turn}')
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                    board()
                    print(f'Ganaste {turn}')
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                    board()
                    print(f'Ganaste {turn}')
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                    board()
                    print(f'Ganaste {turn}')
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                    board()
                    print(f'Ganaste {turn}')
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                    board()
                    print(f'Ganaste {turn}')
                    break

                if count == 9:
                    board()
                    print('Hay empate papa')            

                if turn == '❌':
                    turn = '⭕'
                else:
                    turn = '❌'
            else:
                print('Ya esta ocupada esta casilla, escoge otro')

            
        else:
            print('Introduzca un numero con la posicion del 1 al 9')
    else:
        print('Introduzca un caracter numerico')


