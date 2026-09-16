ROWS = 6
COLUMNS = 7
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

def is_draw(board):
    return legal_moves(board) == []

current_player = "X"
board = create_board()

    
while True:
    print_board(board)
    try:
        column = int(input(f"Player {current_player}, choose a column (1-7): "))
    except ValueError:
        print("Please enter a number from 1 to 7.")
        continue
    
    #need to convert human input to internal calculations
    column -=1
    #check validity
    if column not in legal_moves(board):
        print('Invalid move please choose another column')
        continue
    #apply move
    row = apply_move(board,column,current_player)
    
    #check win
    if is_win(board,row,column):
        print_board(board)
        print(f"Player {current_player} wins ! ")
        break
    #check_draw
    if is_draw(board):
        print_board(board)
        print("Draw! ")
        break
    
    #switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"