# game_rules.py: display rules for player the game
def display_game_rules():
    """
    Display the games rules and the commands to exit the game or start a new partie.
    """
    print("+--------------------------------------------------------------------------+")
    print("|            ############# RULES (TIC TAC TOE) #############               |")
    print("| 1. Two players are required to play this game                            |")
    print("| 2. The Game board is a 3x3-grid                                          |")
    print("| 3. Symbol assigned to each player (p)                                    |")
    print("| 3.1. p1 -> 'X', p2 -> 'O'                                                |")
    print("| 4. Each move is made by two positive digits values separated by a space  |")
    print("|    Example: '1 2' for row 1, column 2                                    |")
    print("| 5. Enter 'q' to quit the game at any time                                |")
    print("| 6. Enter 'y' to play again when game ends                                |")
    print("+--------------------------------------------------------------------------+")
    print()