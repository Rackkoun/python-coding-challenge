# tic_tac_toe.py: main script to run the game
from scripts.game_rules import display_game_rules
from scripts.game_board import init_board, load_board, update_board, display_board
from scripts.players import load_players
from scripts.game_logic import is_valid, check_winner, check_draw

def get_player_move(player_name: str, player_symbol: str, board: list[list[str]]) -> tuple[int, int]:
    "Read and check move enters by a player"
    while True:
        try:
            player_entry = input(f"{player_name} ({player_symbol}) make a move (row col) between [0-2]: ").strip()
            # check if player want to quit
            if player_entry.lower() == 'q':
                return None, None
            player_move = player_entry.split()
            if len(player_move) != 2:
                print("Please enter exactly two numbers separated by space!")
                continue
            row, col = int(player_move[0]), int(player_move[1])

            if not is_valid(board, row, col):
                print("Invalid move! The move is out of the board or already taken. try again.")
                continue
            return row, col
        except ValueError:
            print("Please enter a valide numbers!")
        except (IndexError, KeyboardInterrupt):
            print("\nGame Interrupted!")
            return None, None

def start_game():
    """Main game loop."""
    # 1. Init board and players
    init_board()
    board = load_board()
    P1, P2 = load_players()
    current_player = P1
    
    print("\nGame Started!")
    display_board()

    while True:
        # read player move
        player_name, player_symbol = current_player
        row, col, = get_player_move(player_name, player_symbol, board)

        # check if player want to exit
        if row is None or col is None:
            print(f"Game ended by Player ({player_name})!")
            return False
        
        # Apply the move
        board[row][col] = player_symbol
        update_board(board)
        display_board()

        # Check win case
        if check_winner(board, player_symbol):
            print(f"Congratulation! {player_name} wins!")
            return True
        
        # check draw game case
        if check_draw(board):
            print("It's a draw game!")
            return True
        
        # Switch Player
        current_player = P2 if current_player == P1 else P1

def ask_for_replay_game():
    """Ask if players want to play again"""
    while True:
        choice = input(str("\nWould you like to player again? (y/n): ")).strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no", "q"]:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no." )

# add the whole game in a method
def launch_game():
# 1. Display the rules
    display_game_rules()

    # 2. Run Game in a loop
    while True:
        game_finished = start_game()

        # 2.1. Break the loop in start game if game if player quit game
        # or don't want to play again
        if not game_finished:
            break

        # 2.2. Ask if player want to replay if game is finished or draw
        if not ask_for_replay_game():
            print("Thanks for playing! Goodbye!")
            break

        # Display this message when player want to replay
        print("\n" + "="*25)
        print("Starting a new Party...")
        print("="*25)

if __name__ == '__main__':
    launch_game()