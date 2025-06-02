# Import required modules
import random
import time

# --- Introduction ---
print(f"\033[95mTIC-TAC-TOE, by GROUP 9 <3\033[0m")

# --- Constants ---
PLAYER_X: int = 1
PLAYER_O: int = 2

# --- Game Board Initialization ---
board: list[int] = [0] * 9

# --- Functions ---

def print_board(board_list: list[int]) -> None:
    """
    Prints the current state of the Tic-Tac-Toe board using X and O symbols.

    Args:
        board_list (list[int]): The current board represented as a list of integers.
    """
    print("+---+---+---+")
    for i in range(3):
        row_str = "|"
        for j in range(3):
            index = i * 3 + j
            cell = board_list[index]
            if cell == PLAYER_X:
                row_str += f" \033[91mX\033[0m |"
            elif cell == PLAYER_O:
                row_str += f" \033[92mO\033[0m |"
            else:
                row_str += f" {index + 1} |"
        print(row_str)
        print("+---+---+---+")

def check_win(player: int) -> bool:
    """
    Checks if the given player has won the game.

    Args:
        player (int): The player to check (PLAYER_X or PLAYER_O).

    Returns:
        bool: True if the player has a winning combination, False otherwise.
    """
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combos)

def check_win_on_board(temp_board: list[int], player: int) -> bool:
    """
    Checks if the specified player has a winning combination on a given board.

    Args:
        temp_board (list[int]): The board to check.
        player (int): The player to check for a win.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(temp_board[pos] == player for pos in combo) for combo in win_combos)

def check_possible_win() -> bool:
    """
    Checks if there is still a possible win (no line has both X and O).

    Returns:
        bool: True if a win is still possible, False if it's a guaranteed draw.
    """
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        line = [board[pos] for pos in combo]
        if PLAYER_X not in line or PLAYER_O not in line:
            return True
    return False

def player_move(name: str, symbol: str) -> None:
    """
    Prompts the human player for a move and updates the board.

    Args:
        name (str): The name of the player.
        symbol (str): 'X' or 'O' depending on the player.
    """
    while True:
        move_str = input(f"{name}'s turn ({symbol}). Choose a position (1-9): ").strip()
        try:
            move = int(move_str) - 1
            if move < 0 or move > 8 or board[move] != 0:
                print("Invalid move, try again.")
                continue
            board[move] = PLAYER_X if symbol == 'X' else PLAYER_O
            break
        except ValueError:
            print("Invalid input, enter a number between 1 and 9.")

def computer_move(symbol: str) -> None:
    """
    Determines and makes the computer's move. It blocks the opponent if they can win.

    Args:
        symbol (str): The computer's symbol ('X' or 'O').
    """
    empty_positions = [i for i, spot in enumerate(board) if spot == 0]
    computer = PLAYER_X if symbol == 'X' else PLAYER_O
    opponent = PLAYER_O if computer == PLAYER_X else PLAYER_X

    for move in empty_positions:
        board_copy = board.copy()
        board_copy[move] = opponent
        if check_win_on_board(board_copy, opponent):
            board[move] = computer
            print(f"Computer chose position {move + 1}")
            return

    move = random.choice(empty_positions)
    board[move] = computer
    print(f"Computer chose position {move + 1}")

def ask_play_again() -> None:
    """
    Asks the user if they want to play again and restarts or exits the game accordingly.
    """
    while True:
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again in ['y', 'yes']:
            play_game()
            break
        elif again in ['n', 'no']:
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")

def get_valid_name(prompt: str) -> str:
    """
    Prompts the user to enter a valid player name.

    Args:
        prompt (str): The prompt message to display.

    Returns:
        str: A valid name input from the user.
    """
    while True:
        name = input(prompt).strip().title()
        if not name:
            print("Invalid input. Please enter a name.")
        elif name.lower() == "computer":
            print("The name 'Computer' is reserved. Please select another name.")
        else:
            return name

def play_game() -> None:
    """
    Starts and controls the flow of the Tic-Tac-Toe game,
    including setup, player turns, win checking, and replay option.
    """
    global board
    board = [0] * 9

    print("GAME MODE")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    while True:
        mode = input("Pick an option [1 - 2]: ").strip()
        if mode in ['1', '2']:
            break
        print("Invalid selection. Please choose 1 or 2.")

    if mode == '1':
        p1 = get_valid_name("Enter name for Player 1: ")
        p2 = get_valid_name("Enter name for Player 2: ")
    else:
        p1 = get_valid_name("Enter your name: ")
        p2 = "Computer"

    print("\nSELECT THE 'X' PLAYER")
    print("1. First")
    print("2. Second")
    print("3. Random")
    while True:
        choice = input("Pick an option [1 - 3]: ").strip()
        if choice == '1':
            x_player = p1
            o_player = p2
            break
        elif choice == '2':
            x_player = p2
            o_player = p1
            break
        else:
            random_pick = random.choice([True, False])
            x_player = p1 if random_pick else p2
            o_player = p2 if random_pick else p1
            break

    print(f"\n{x_player} will be X.")
    print(f"{o_player} will be O.\n")

    turns = 0
    current_player = PLAYER_X

    if mode == '2' and x_player == "Computer":
        print_board(board)
        print(f"{x_player}'s turn (X).")
        print("Computer is thinking... 💭")
        time.sleep(2)
        computer_move('X')
        turns += 1
        current_player = PLAYER_O

    while True:
        print_board(board)
        name = x_player if current_player == PLAYER_X else o_player
        symbol = 'X' if current_player == PLAYER_X else 'O'

        if mode == '1' or name != "Computer":
            player_move(name, symbol)
        else:
            print(f"{name}'s turn ({symbol}).")
            print("Computer is thinking... 💭")
            time.sleep(2)
            computer_move(symbol)

        turns += 1

        if check_win(current_player):
            time.sleep(2)
            print_board(board)
            print(f"\n{name}({symbol}) wins!")
            break

        if turns == 9 or not check_possible_win():
            time.sleep(2)
            print_board(board)
            print("\nWell played!, the match ended as a draw.")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    ask_play_again()

# Start the game
play_game()
