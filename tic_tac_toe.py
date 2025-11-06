from scripts.game_rules import display_game_rules
from scripts.game_board import init_board
from scripts.players import load_players

if __name__ == '__main__':
    # 1. Display the rules
    display_game_rules()

    # 2. init the game
    init_board()

    # 3. play
    is_playing = True
    # 3.1. Load players
    P1, P2 = load_players()
    print(P1)
    # prompt 1
    
    # print(prompt1)

    # first check here
    while is_playing:
        # prompt1 = str(input(f"{P1[0]} make a move (x1, x2) between [0 - 2]: ")).split(' ')
        # try:
        #     row, col = int(prompt1[0]), int(prompt1[1])
        #     if not (0 <= row <= 2 and 0 <= col <= 2):
        #         prompt1_again = True
        #         while prompt1_again:
        #             pass
        pass

