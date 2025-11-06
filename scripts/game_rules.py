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
    print("| 5. each move is made by two positives digits values separated by a space |")
    print("| 5. the next player will be asked to play when the previous will provide  |")
    print("| 5. a correct entry value                                                 |")
    print("| 5. Enter 'y' to play again or 'q' tu exit the game                       |")
    print("+--------------------------------------------------------------------------+")