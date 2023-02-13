"""
Tic Tac Toe
"""
import random


class TicTacToe:

    def __init__(self):
        """
        Create empty board once object created
        """
        self.board = []

    def create_board(self):
        """
        Create 3x3 board with empty slots
        """
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    def show_board(self):
        """
        Show 3x3 board in presentable fashion
        """
        for row in self.board:
            for item in row:
                print(item, end="  ")
            # print empty line
            print("")

    def get_random_first_player(self):
        """
        Returns random number 0 or 1
        """
        return random.randint(0, 1)

    def swap_player_turn(self, player):
        """
        Swaps current player
        """
        if player == "0":
            return "X"
        else:
            return "0"

    def draw_symbol(self, row, col, player):
        """
        Draw players symbol in the selected position
        """
        self.board[row][col] = player

    def has_player_won(self, player):
        """
        Check rows, columns and diagonals using set() to confirm 3 in a row of one symbol
        """
        board_len = len(self.board)
        board_values = set()

        # check rows
        for i in range(board_len):
            for j in range(board_len):
                board_values.add(self.board[i][j])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check columns
        for i in range(board_len):
            for j in range(board_len):
                board_values.add(self.board[j][i])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check diagonals
        for i in range(board_len):
            board_values.add(self.board[i][i])
        if board_values == {player}:
            return True
        else:
            board_values.clear()

        # edge diagonal condition
        board_values.add(self.board[2][0])
        board_values.add(self.board[1][1])
        board_values.add(self.board[0][2])
        if board_values == {player}:
            return True
        else:
            return False

    def is_board_filled(self):
        """
        Check to see if the board has any empty slots. If not, board is filled.
        """
        for row in self.board:
            for item in row:
                if item == "-":
                    return False
        return True

    def start(self):
        """
        Run the game
        """

        self.create_board()
        if self.get_random_first_player() == 0:
            player = "0"
        else:
            player = "X"
        game_over = False

        while not game_over:
            try:
                # show board and what player starts
                self.show_board()
                print(f"Player {player}'s turn")

                # use map to convert iterable input into int and then a list
                row, col = list(map(int, input("Enter row and column to place symbol e.g. '1 3': ").split()))
                print("")

                # if only row is given raise a valueError
                if col is None:
                    raise ValueError("Not enough values to unpack: expected 2")

                # draw symbol in position specified
                self.draw_symbol(row - 1, col - 1, player)

                # check if player has won
                game_over = self.has_player_won(player)
                if game_over:
                    print(f"Player {player} has won the game!")
                    continue

                # check if board is filled
                game_over = self.is_board_filled()
                if game_over:
                    print("The match is a draw!")
                    continue

                # since game hasn't ended, swap player
                player = self.swap_player_turn(player)

            except ValueError as err:
                print(err)

        print("testing commit and push through pycharm")
        print()
        self.show_board()


if __name__ == '__main__':
    game = TicTacToe()
    game.start()
