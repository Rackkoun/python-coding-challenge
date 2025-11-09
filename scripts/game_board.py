# board_game.py: manage the board

board: list[list[str]] = []

def init_board():
    global board
    board = []
    for _ in range(3):
        board.append([''] * 3)

def load_board() -> list[list[str]]:
    return board

def update_board(b: list[list[str]]) -> list[list[str]]:
    global board
    board = b
    return board

def display_board():
    """
    Display the current state of the game board.
    """
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" ", end="")
        for j, col in enumerate(row):
            symbol = col if col else " "
            print(f" {symbol} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print(" -----------")
    print()