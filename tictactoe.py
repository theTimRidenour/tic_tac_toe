
from os import name, system

choices = [0] * 9
option_screen = ['   7 | 8 | 9', '   4 | 5 | 6', '   1 | 2 | 3']

def board(choices = choices):
    ''' Build the tic-tac-toe board, and
     and Xs for user and Os for computer
     choices. '''
    if choices[6] == 1:
        print (' X ', end = '|')
    elif choices[6] == 2:
        print (' O ', end = '|')
    else:
        print ('   ', end = '|')
    
    if choices[7] == 1:
        print (' X ', end = '|')
    elif choices[7] == 2:
        print (' O ', end = '|')
    else:
        print ('   ', end = '|')

    if choices[8] == 1:
        print (' X ', option_screen[0])
    elif choices[8] == 2:
        print (' O ', option_screen[0])
    else:
        print ('   ', option_screen[0])

    print('---+---+---   ---+---+---')

    if choices[3] == 1:
        print (' X ', end = '|')
    elif choices[3] == 2:
        print (' O ', end = '|')
    else:
        print ('   ', end = '|')
    
    if choices[4] == 1:
        print (' X ', end = '|')
    elif choices[4] == 2:
        print (' O ', end = '|')
    else:
        print ('   ', end = '|')

    if choices[5] == 1:
        print (' X ', option_screen[1])
    elif choices[5] == 2:
        print (' O ', option_screen[1])
    else:
        print ('   ', option_screen[1])

    print('---+---+---   ---+---+---')
    
    if choices[0] == 1:
        print (' X ', end = '|')
    elif choices[0] == 2:
        print (' O ', end = '|')
    else:
        print ('   ', end = '|')
    
    if choices[1] == 1:
        print (' X ', end = '|')
    elif choices[1] == 2:
        print (' O ', end = '|')
    else:
        print ('   ', end = '|')

    if choices[2] == 1:
        print (' X ', option_screen[2])
    elif choices[2] == 2:
        print (' O ', option_screen[2])
    else:
        print ('   ', option_screen[2])

def check_if_winner(choices = choices, player = 1):
    title()
    
    # check if the user has won the game.
    if (choices[0] == 1 and choices[1] == 1 and choices[2] == 1) or (choices[3] == 1 and choices[4] == 1 and choices[5] == 1) or (choices[6] == 1 and choices[7] == 1 and choices[8] == 1) or (choices[0] == 1 and choices[3] == 1 and choices[6] == 1) or (choices[1] == 1 and choices[4] == 1 and choices[7] == 1) or (choices[2] == 1 and choices[5] == 1 and choices[8] == 1) or (choices[0] == 1 and choices[4] == 1 and choices[8] == 1) or (choices[2] == 1 and choices[4] == 1 and choices[6] == 1):
        print ('CONGRADULATIONS YOU HAVE WON!\n')
        board(choices)
        if input('\nDo you want to play again? yes/no ').lower() == 'yes':
            check_if_winner([0, 0, 0, 0, 0, 0, 0, 0, 0]) # clear game board.
    
    # check if computer has won the game.
    elif (choices[0] == 2 and choices[1] == 2 and choices[2] == 2) or (choices[3] == 2 and choices[4] == 2 and choices[5] == 2) or (choices[6] == 2 and choices[7] == 2 and choices[8] == 2) or (choices[0] == 2 and choices[3] == 2 and choices[6] == 2) or (choices[1] == 2 and choices[4] == 2 and choices[7] == 2) or (choices[2] == 2 and choices[5] == 2 and choices[8] == 2) or (choices[0] == 2 and choices[4] == 2 and choices[8] == 2) or (choices[2] == 2 and choices[4] == 2 and choices[6] == 2):
        print('SORRY YOU HAVE LOST.')
        board(choices)
        if input('\nDo you want to play again? yes/no ').lower() == 'yes':
            check_if_winner([0, 0, 0, 0, 0, 0, 0, 0, 0]) # clear game board

    # check if board is filled, but no one as won.
    elif choices[0] != 0 and choices[1] != 0 and choices[2] != 0 and choices[3] != 0 and choices[4] != 0 and choices[5] != 0 and choices[6] != 0 and choices[7] != 0 and choices[8] != 0:
        print('TIE GAME, BETTER LUCK NEXT TIME.')
        board(choices)
        if input('\nDo you want to play again? yes/no ').lower() == 'yes':
            check_if_winner([0, 0, 0, 0, 0, 0, 0, 0, 0]) # clear game board
    else:
        if player == 2:
            computer_move(choices)
        else:
            board(choices) # display updated board
            make_selection(choices)

def computer_move(choices = choices):

    # check if computer can win, and choose winning spot.
    if choices[0] == 2 and choices[1] == 2 and choices[2] == 0:
        choices[2] = 2
    elif choices[3] == 2 and choices[4] == 2 and choices[5] == 0:
        choices[5] = 2
    elif choices[6] == 2 and choices[7] == 2 and choices[8] == 0:
        choices[8] = 2
    elif choices[0] == 2 and choices[1] == 0 and choices[2] == 2:
        choices[1] = 2
    elif choices[3] == 2 and choices[4] == 0 and choices[5] == 2:
        choices[4] = 2
    elif choices[6] == 2 and choices[7] == 0 and choices[8] == 2:
        choices[7] = 2
    elif choices[0] == 0 and choices[1] == 2 and choices[2] == 2:
        choices[0] = 2
    elif choices[3] == 0 and choices[4] == 2 and choices[5] == 2:
        choices[3] = 2
    elif choices[6] == 0 and choices[7] == 2 and choices[8] == 2:
        choices[6] = 2
    elif choices[0] == 2 and choices[3] == 2 and choices[6] == 0:
        choices[6] = 2
    elif choices[1] == 2 and choices[4] == 2 and choices[7] == 0:
        choices[7] = 2
    elif choices[2] == 2 and choices[5] == 2 and choices[8] == 0:
        choices[8] = 2
    elif choices[0] == 2 and choices[3] == 0 and choices[6] == 2:
        choices[3] = 2
    elif choices[1] == 2 and choices[4] == 0 and choices[7] == 2:
        choices[4] = 2
    elif choices[2] == 2 and choices[5] == 0 and choices[8] == 2:
        choices[5] = 2
    elif choices[0] == 0 and choices[3] == 2 and choices[6] == 2:
        choices[0] = 2
    elif choices[1] == 0 and choices[4] == 2 and choices[7] == 2:
        choices[1] = 2
    elif choices[2] == 0 and choices[5] == 2 and choices[8] == 2:
        choices[2] = 2
    elif choices[0] == 2 and choices[4] == 2 and choices[8] == 0:
        choices[8] = 2
    elif choices[0] == 2 and choices[4] == 0 and choices[8] == 2:
        choices[4] = 2
    elif choices[0] == 0 and choices[4] == 2 and choices[8] == 2:
        choices[0] = 2
    elif choices[2] == 2 and choices[4] == 2 and choices[6] == 0:
        choices[6] = 2
    elif choices[2] == 2 and choices[4] == 0 and choices[6] == 2:
        choices[4] = 2
    elif choices[2] == 0 and choices[4] == 2 and choices[6] == 2:
        choices[2] = 2

    # check if player can win and block player.
    elif choices[0] == 1 and choices[1] == 1 and choices[2] == 0:
        choices[2] = 2
    elif choices[3] == 1 and choices[4] == 1 and choices[5] == 0:
        choices[5] = 2
    elif choices[6] == 1 and choices[7] == 1 and choices[8] == 0:
        choices[8] = 2
    elif choices[0] == 1 and choices[1] == 0 and choices[2] == 1:
        choices[1] = 2
    elif choices[3] == 1 and choices[4] == 0 and choices[5] == 1:
        choices[4] = 2
    elif choices[6] == 1 and choices[7] == 0 and choices[8] == 1:
        choices[7] = 2
    elif choices[0] == 0 and choices[1] == 1 and choices[2] == 1:
        choices[0] = 2
    elif choices[3] == 0 and choices[4] == 1 and choices[5] == 1:
        choices[3] = 2
    elif choices[6] == 0 and choices[7] == 1 and choices[8] == 1:
        choices[6] = 2
    elif choices[0] == 1 and choices[3] == 1 and choices[6] == 0:
        choices[6] = 2
    elif choices[1] == 1 and choices[4] == 1 and choices[7] == 0:
        choices[7] = 2
    elif choices[2] == 1 and choices[5] == 1 and choices[8] == 0:
        choices[8] = 2
    elif choices[0] == 1 and choices[3] == 0 and choices[6] == 1:
        choices[3] = 2
    elif choices[1] == 1 and choices[4] == 0 and choices[7] == 1:
        choices[4] = 2
    elif choices[2] == 1 and choices[5] == 0 and choices[8] == 1:
        choices[5] = 2
    elif choices[0] == 0 and choices[3] == 1 and choices[6] == 1:
        choices[0] = 2
    elif choices[1] == 0 and choices[4] == 1 and choices[7] == 1:
        choices[1] = 2
    elif choices[2] == 0 and choices[5] == 1 and choices[8] == 1:
        choices[2] = 2
    elif choices[0] == 1 and choices[4] == 1 and choices[8] == 0:
        choices[8] = 2
    elif choices[0] == 1 and choices[4] == 0 and choices[8] == 1:
        choices[4] = 2
    elif choices[0] == 0 and choices[4] == 1 and choices[8] == 1:
        choices[0] = 2
    elif choices[2] == 1 and choices[4] == 1 and choices[6] == 0:
        choices[6] = 2
    elif choices[2] == 1 and choices[4] == 0 and choices[6] == 1:
        choices[4] = 2
    elif choices[2] == 0 and choices[4] == 1 and choices[6] == 1:
        choices[2] = 2
    
    # if no one can win choose empty slot
    #     check middle first
    #     then check centers
    #     finally check corners
    elif choices[4] == 0:
        choices[4] = 2
    elif choices[1] == 0:
        choices[1] = 2
    elif choices[3] == 0:
        choices[3] = 2
    elif choices[5] == 0:
        choices[5] = 2
    elif choices[7] == 0:
        choices[7] = 2
    elif choices[0] == 0:
        choices[0] = 2
    elif choices[2] == 0:
        choices[2] = 2
    elif choices[6] == 0:
        choices[6] = 2
    elif choices[8] == 0:
        choices[8] = 2

    # default starting position for computer
    # TODO: add choice for computer to go first
    else:
        choices[2] = 2
    
    check_if_winner(choices)

def make_selection(choices = choices):
    selc = int(input('\nPick a number 1 - 9: '))
    if selc > 9 or selc < 1:
        print('Must be a number between 1 - 9')
        make_selection(choices)
    elif choices[selc - 1] != 0:
        print('Spot already taken')
        make_selection(choices)
    else:
        choices[selc - 1] = 1
        check_if_winner(choices, 2)

def title():
    if name == 'nt': # clear screen for windows
        _ = system('cls')
    else:            # clear screen for unix (mac/linux) and others
        _ = system('clear')
    print ('Tic-Tac-Toe\n')

if __name__ == '__main__':
    check_if_winner()