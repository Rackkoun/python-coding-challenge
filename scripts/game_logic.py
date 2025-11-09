# game_logic.py: This script contains the game logic like checking win, draw game and valid move situation made by a player

def is_valid(board: list[list[str]], row: int, col: int) -> bool:
    """Check if the move made by the current player is valid or not."""
    # check if the entry for row and col are inside the grid size and
    # if the location in the grid is empty.
    return (0 <= row <= 2) and (0 <= col <= 2) and board[row][col] == ""

def check_winner(board: list[list[str]], player_symbol: str) -> bool:
    pass