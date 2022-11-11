board = list(range(1, 10))

win_lines = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 3, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3],'|', board[2+i*3], '|')
        print('-------------')

def take_input(player_token):
    while True:
        value = input('Куда поставить: '+ player_token + '?')
        if value not in '123456789':
            print('вели неправильно')
            continue
        value = int(value)
        if str(board[value-1]) in 'XO':
            print('Эта клетка занята')
            continue
        board[value-1] = player_token
        break
def check_win():
    for each in win_lines:
        if board([each[0]-1] == board[1]-1 == board[2]-1):
            return board[each[1]-1]
        else:
            return False
def main():
    



draw_board()
take_input('X')
take_input('O')

