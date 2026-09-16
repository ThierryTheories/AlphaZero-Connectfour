ROWS = 6
COLUMNS = 7

current_player = "X"
def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    
    for row in board:
        print("|" +  "|".join(row) + "|")
    print("-" * (COLUMNS * 3 - 6))
    print(" 1 2 3 4 5 6 7")
    
def apply_move(board, column, current_player):
    
    row = ROWS -1
    while row >=0:
        if board[row][column] != " ":
            row -= 1
        else:
            board[row][column] = current_player
            return row
        

def legal_moves(board):
    legal_list = []
    for i in range(COLUMNS):
        if board[0][i] == " ":
            legal_list.append(i)
    return legal_list
    
def is_win(board,row,col):
    directions = [
    (0, 1),   # horizontal
    (1, 0),   # vertical
    (1, 1),   # diagonal
    (1, -1)   # diagonal
    ]
    piece = board[row][col]
    
    if piece == " ":
        return False
    
    for dr,dc in directions:
        count = 1
        
    #check one direction first
        current_row = row
        current_col = col
        
        while True:
            current_row += dr
            current_col +=dc
            if current_row < 0 or current_row >= ROWS or current_col < 0 or current_col >= COLUMNS:
                break
            if board[current_row][current_col] != piece:
                break
            count +=1
        
        #CHECK OPPOSITE DIRECTION
        current_row = row
        current_col = col
        while True:
            current_row -= dr
            current_col -=dc
            if current_row < 0 or current_row >= ROWS or current_col < 0 or current_col >= COLUMNS:
                    break
            if board[current_row][current_col] != piece:
                    break
            count +=1
        
        if count >= 4:
            return True
    return False


board = create_board()

row = apply_move(board, 0, "X")
row = apply_move(board, 1, "X")
row = apply_move(board, 2, "X")
row = apply_move(board, 3, "X")

print(is_win(board, row, 3))