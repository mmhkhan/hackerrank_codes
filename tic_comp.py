import random
board = ['-','-','-','-','-','-','-','-','-']
current_player = input('choose either X or O: ')
init_player = current_player
comp_list = ['1','2','3','4','5','6','7','8','9']
game_going = True


def display_board():
    global current_player
    print(board[0] + '|'+ board[1] + '|' + board[2]+'     1|2|3')
    print(board[3] + '|'+ board[4] + '|' + board[5]+'     4|5|6')
    print(board[6] + '|'+ board[7] + '|' + board[8]+'     7|8|9')
    handle_turn(current_player)

def play_game():
    display_board()


def check_game_over():

    if check_for_winner():
        print(check_for_winner() + ' won')
        print(board[0] + '|' + board[1] + '|' + board[2] + '     1|2|3')
        print(board[3] + '|' + board[4] + '|' + board[5] + '     4|5|6')
        print(board[6] + '|' + board[7] + '|' + board[8] + '     7|8|9')
        game_going = False
    elif '-' not in board:
        print('Tie')
        game_going = False
    else:
        flip_player()


def check_for_winner():
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return winner

def check_rows():
    row_1 = board[0] == board[1]==board[2]!= '-'
    row_2 = board[3] == board[4]==board[5]!= '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    col_1 = board[0] == board[3]==board[6]!= '-'
    col_2 = board[1] == board[4]==board[7]!= '-'
    col_3 = board[2] == board[5] == board[8] != '-'
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None
def check_diagonals():
    dia_1 = board[0] == board[4]==board[8]!= '-'
    dia_2 = board[2] == board[4]==board[6]!= '-'
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    else:
        return None

def handle_turn(player):
    global current_player
    global comp_list
    print(player + "'s turn")
    if player==init_player:
        position = input('Input any number between 1 and 9: ')
        if position not in ['1','2','3','4','5','6','7','8','9']:
            print('Pay attention! Input any number between 1 and 9: ')
        elif board[int(position)-1]!='-':
            print("Don't mess with me. Go again: ")
        else: board[int(position)-1] = player
    else:
        position = random.choice(comp_list)
        if board[int(position) - 1]==init_player:
            comp_list.remove(position)
            position = random.choice(comp_list)
        board[int(position) - 1] = player
    check_game_over()

def flip_player():
    global current_player
    if current_player == 'X': current_player = 'O'
    elif current_player == 'O': current_player = 'X'

    display_board()

play_game()