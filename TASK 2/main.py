import math

# Constants for the players
AI = 'O'
YOU = 'X'

# Initialize the board
def initialize_board():
    return ['-'] * 9

# Function to display the board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
    print()

# Check if a player has won
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

# Check if the board is full
def is_board_full(board):
    return all(cell != '-' for cell in board)

# Minimax algorithm with alpha-beta pruning
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, AI):
        return 10 - depth
    elif check_winner(board, YOU):
        return depth - 10
    elif is_board_full(board):
        return 0

    if maximizing_player:  # AI's turn
        max_eval = -math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = AI
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = '-'
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:  # Player's turn
        min_eval = math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = YOU
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = '-'
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Find the AI's best move
def find_best_move(board):
    best_move = -1
    best_eval = -math.inf
    for i in range(9):
        if board[i] == '-':
            board[i] = AI
            eval = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = '-'
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. AI is 'O'.")
    print("Make your move by selecting a number (0-8):\n")
    
    while True:
        print_board(board)
        
        # Player's move
        try:
            move = int(input("Your move (0-8): "))
            if move < 0 or move > 8 or board[move] != '-':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 0 and 8.")
            continue
        
        board[move] = YOU
        if check_winner(board, YOU):
            print_board(board)
            print("Congratulations, you win! 🎉")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # AI's move
        print("AI is thinking...")
        ai_move = find_best_move(board)
        board[ai_move] = AI
        print(f"AI chose position {ai_move}.\n")
        if check_winner(board, AI):
            print_board(board)
            print("AI wins! Better luck next time! 🤖")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

# Start the game
if __name__ == "__main__":
    play_game()
