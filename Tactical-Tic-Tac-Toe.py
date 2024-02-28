class UltimateTicTacToe:
    def __init__(self):
        self.board = [[' ']*9 for _ in range(9)]
        self.current_board = None
        self.current_player = 'X'
        self.winner = None

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 17)

    def print_small_boards(self):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    print(f'{self.board[i*3+k][j*3]} | {self.board[i*3+k][j*3+1]} | {self.board[i*3+k][j*3+2]}    ', end='')
                print('\n' + '-' * 29)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_move(self, row, col):
        if self.winner:
            print(f"Player {self.winner} has already won!")
            return

        if self.current_board is not None and self.board[row][col] == ' ' and self.current_board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_board = None
            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                self.winner = self.current_player
            else:
                self.switch_player()
        elif self.current_board is None and self.board[row][col] == ' ':
            self.current_board = [[None]*3 for _ in range(3)]
        else:
            print("Invalid move. Try again.")

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True

        # Check small boards
        for i in range(3):
            for j in range(3):
                if self.check_small_board_winner(i, j):
                    return True

        return False

    def check_small_board_winner(self, row, col):
        board = self.current_board if self.current_board is not None else self.board
        return all(board[row*3+k][col*3] == self.current_player for k in range(3)) or \
               all(board[row*3+k][col*3+1] == self.current_player for k in range(3)) or \
               all(board[row*3+k][col*3+2] == self.current_player for k in range(3))

if __name__ == "__main__":
    game = UltimateTicTacToe()

    while not game.winner:
        game.print_small_boards()
        print(f"Player {game.current_player}'s turn.")
        try:
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-8): "))
            game.make_move(row, col)
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Player {game.winner} wins the Ultimate Tic Tac Toe game!")
