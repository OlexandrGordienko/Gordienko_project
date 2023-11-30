from random import choice

def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        for _ in range(3):
            print("|       ", end="")
        print("|")
        for square in row:
            print("|   " + square + "   ", end="")
        print("|")
        for _ in range(3):
            print("|       ", end="")
        print("|")
    print("+-------" * 3 + "+")

def enter_move(board):
    while True:
        move = int(input("Введіть свій хід: ")) - 1
        row = move // 3
        col = move % 3
        if 0 <= row <= 2 and 0 <= col <= 2 and (board[row][col] == " " or board[row][col].isdigit()):
            board[row][col] = "O"
            break
        else:
            print("Невірний хід. Спробуйте ще раз.")

def make_list_of_free_fields(board):
    return [(i, j) for i, row in enumerate(board) for j, square in enumerate(row) if square == " " or square.isdigit()]

def victory_for(board, sign):
    for i in range(3):
        if all(cell == sign for cell in board[i]) or all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = choice(free_fields)
        board[move[0]][move[1]] = "X"

# Тест функції
board = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
board[1][1] = "X"
while True:
    display_board(board)
    if victory_for(board, "X"):
        print("Переміг комп'ютер :(")
        break
    elif victory_for(board, "O"):
        print("Ти переміг!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("Нічия!")
        break
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        display_board(board)
        print("Ти переміг!")
        break
    draw_move(board)