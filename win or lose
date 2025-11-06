# winner or draw check

def check_winner(board):
    players = ["X", "O"]
    for player in players:
        # check rows and colums
        for i in range(3):
            if all (board[i][j] == player for j in range(3)) or all (board[j][i] == player for j in range(3)):
                return f"{player} wins"
        # check diagonals
        if all (board[i][i] == player for i in range(3)) or all (board[i][2-i] == player for i in range(3)):
            return f"{player} wins"
        
    # check for draw or ongoing game
    if all (cell in ["X", "O"] for row in board for cell in row):
        return "Draw"
    else:
        return "Game ongoing"
# Example usage
board = [
    ["X", "O", "X"],
    ["X", "X", "O"],
    ["O", "X", "O"]
]
result = check_winner(board)
print(result)  # Output: Draw
