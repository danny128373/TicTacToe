# Display board
# Ask player 1 if they want to be X or 0
# Display board (made of strings)
# Player 1 input (int 1-9) and replace blank position. Perhaps using format and {}
#   for the position the player picks
# Player 2 input (int 1-9) and replace blank position
'''
Ask if players are ready - done
Ask if player 1 is X or 0
Accept input Yes or No
Display board (made of strings with a {} which can be replaced for inputs)
Ask for player 1 input
Display board with player 1's input
Ask for player 2 input
Display board with player 2's input
...
Method to check when 3 in a row has been accomplished
Print result of game
'''
import sys

tictactoe1 = '   |   |   \n'
tictactoe2 = '-----------\n'
tictactoe3 = '   |   |   \n'
tictactoe4 = '-----------\n'
tictactoe5 = '   |   |   '


def are_you_ready():
    print('Are you guys ready to play the best game ever of tick tac toe?')
    answer = str(input())
    if answer.lower() == 'yes':
        print('Prepare to destroy your opponent or be destroyed, who knows?')
        print("Player 1, would you like to be X's or O's")
    else:
        print('You probably were going to lose anyway')
        sys.exit()


def first_turn():
    if x_or_o.lower() == 'x':
        print('Player 1 goes first')
    else:
        print('Player 2 goes first')


def display_board():
    print(tictactoe1 + tictactoe2 + tictactoe3 + tictactoe4 + tictactoe5)


are_you_ready()
x_or_o = str(input())
first_turn()
display_board()
print('Select the position')
position = int(input())
if position == 1:
        tictactoe5 = tictactoe5[0] + 'X' + tictactoe5[2:]
elif position == 2:
        tictactoe5 = tictactoe5[:5] + 'X' + tictactoe5[6:]
elif position == 3:
        tictactoe5 = tictactoe5[:9] + 'X' + tictactoe5[10:]
elif position == 4:
        tictactoe3 = tictactoe3[0] + 'X' + tictactoe3[2:]
elif position == 5:
        tictactoe3 = tictactoe3[:5] + 'X' + tictactoe3[6:]
elif position == 6:
        tictactoe3 = tictactoe3[:9] + 'X' + tictactoe3[10:]
elif position == 7:
        tictactoe1 = tictactoe1[0] + 'X' + tictactoe1[2:]
elif position == 8:
        tictactoe1 = tictactoe1[:5] + 'X' + tictactoe1[6:]
elif position == 9:
        tictactoe1 = tictactoe1[:9] + 'X' + tictactoe1[10:]
else:
        print('Input not valid, please choose from position 1-9')
        position = int(input())
display_board()
