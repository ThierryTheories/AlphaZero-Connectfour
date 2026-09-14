ROWS = 6
COLUMNS = 7

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    
    for row in board:
        print("|" +  "|".join(row) + "|")
    print("-" * (COLUMNS * 3 - 6))
    print(" 1 2 3 4 5 6 7")
    

board = create_board()
print_board(board)  