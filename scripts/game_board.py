# board_game.py: manage the board

# [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
# ]
board: list[list[str]] = []
def init_board():
    for _ in range(3):
        board.append([''] * 3)
    print(board)


