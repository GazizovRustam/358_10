import os


def main():
    newGame = 'y'
    continues = 'y'
    start = False
    try:
        newGame = input('New Game ? Y/n ')

        quantityUser = int(input('Quantity user: '))

        if newGame == 'y' or newGame == 'Y':
            start = create_play(quantityUser)
        else:
            continues = update_value_game(quantityUser)

        if start:
            continues = update_value_game(quantityUser)

        if continues == 'n' or continues == 'N':
            total_points()
    except ValueError:
        print('Invalid value entered')


def create_play(quantityUser) -> bool:

    points = 0.0
    try:
        with open('game.txt', 'w') as fw:

            for i in range(quantityUser):

                name = input('Name: ')

                fw.write(name + '\n')
                fw.write(str(points) + '\n')

    except ValueError:
        print('Invalid value entered!')
    return True



def update_value_game(quantityUser) -> str:
    print('Start the game!')
    continues = 'y'

    while continues == 'y' or continues == 'Y':

        for i in range(1, quantityUser + 1):
            search = input('Player {}: '.format(i))
            addValue = float(input('Add value: '))

            with open('game.txt', 'r') as fr:

                with open('temp_file.txt', 'a') as fa:

                    descr = fr.readline()

                    while descr != '':

                        qty = float(fr.readline())

                        descr = descr.strip('\n')

                        if descr == search:
                            fa.write(descr + '\n')
                            total = qty + addValue
                            fa.write(str(total) + '\n')

                        else:
                            fa.write(descr + '\n')
                            fa.write(str(qty) + '\n')

                        descr = fr.readline()

            os.remove('game.txt')
            os.rename('temp_file.txt', 'game.txt')

        continues = input('Are the game continues? Y/n  ')

    return continues


def total_points():
    with open('game.txt', 'r') as fr:

        descr = fr.readline()

        while descr != '':
            qty = float(fr.readline())

            descr = descr.strip()

            print('Player {}, total points: {}'.format(descr, qty))

            descr = fr.readline()


main()

