# game_logic.py: This script contains the game logic like checking win, draw game and valid move situation made by a player

def is_valid(board: list[list[str]], row: int, col: int) -> bool:
    """Check if the move made by the current player is valid or not."""
    # check if the entry for row and col are inside the grid size and
    # if the location in the grid is empty.
    return (0 <= row <= 2) and (0 <= col <= 2) and board[row][col] == ""

def check_winner(board: list[list[str]], player_symbol: str) -> bool:
    """Check if the current player has won."""
    # 1. Rows check
    for row in board:
        # all func :-> return true of all elem in the iter are true/empty.
        if all(cell == player_symbol for cell in row):
            return True
    
    # 2. Cols check
    for col in range(3):
        if all(board[row][col] == player_symbol for row in range(3)):
            return True
    
    # 3. Diagonal check
    # 3.1. Normal diag
    if all(board[i][i] == player_symbol for i in range(3)):
        return True
    # 3.2. Reverse diag
    if all(board[i][2-i] == player_symbol for i in range(3)):
        return True
    
    return False

def check_draw(board: list[list[str]]) -> bool:
    """Check if no winner"""
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True