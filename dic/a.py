class MagnetsGame:
    def __init__(self, size, pos_of_magnets, pos_of_stones, pos_of_empty):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.pos_of_magnets = pos_of_magnets
        self.pos_of_stones = pos_of_stones
        self.pos_of_empty = pos_of_empty
        self.place_initial_positions()

    def place_initial_positions(self):
        for pos in self.pos_of_stones:
            self.board[pos[0]][pos[1]] = '0'
        for pos in self.pos_of_magnets:
            self.board[pos[0]][pos[1]] = 'x'
        for pos in self.pos_of_empty:
            self.board[pos[0]][pos[1]] = 'o'

    def is_valid(self, row, col):
        if self.board[row][col] != '.':
            return False
        for i in range(max(0, row-1), min(self.size, row+2)):
            for j in range(max(0, col-1), min(self.size, col+2)):
                if self.board[i][j] == 'x':
                    return False
        return True

    def solve(self):
        return self.backtrack(0, 0)

    def backtrack(self, row, col):
        if row == self.size:
            return True
        if col == self.size:
            return self.backtrack(row + 1, 0)
        if self.board[row][col] != '.':
            return self.backtrack(row, col + 1)

        if self.is_valid(row, col):
            self.board[row][col] = 'x'
            if self.backtrack(row, col + 1):
                return True
            self.board[row][col] = '.'

        if self.backtrack(row, col + 1):
            return True

        return False

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

def load_level(level):
    levels = {
        1: {
            'size': 4,
            'pos_of_magnets': [(0, 0)],
            'pos_of_stones': [(1, 1), (2, 2)],
            'pos_of_empty': [(0, 1), (1, 0)]
        },
        2: {
            'size': 5,
            'pos_of_magnets': [(0, 0), (1, 2)],
            'pos_of_stones': [(2, 2), (3, 3)],
            'pos_of_empty': [(0, 1), (1, 0), (4, 4)]
        }
        # Add more levels as needed
    }
    return levels[level]

# Example usage
for level in range(1, 3):  # Adjust range for the number of levels
    level_data = load_level(level)
    game = MagnetsGame(level_data['size'], level_data['pos_of_magnets'], level_data['pos_of_stones'], level_data['pos_of_empty'])
    print(f"Solving level {level}...")
    if game.solve():
        game.print_board()
    else:
        print("No solution found")
    print("\n" + "="*20 + "\n")
