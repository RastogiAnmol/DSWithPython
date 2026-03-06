import math

GRID_SIZE = 8

def solve_queens():
    results = []
    # We use a 1D array to represent the board
    # columns[row] = column_index
    columns = [-1] * GRID_SIZE
    
    def place_queens(row):
        # BASE CASE: We reached the end! All queens placed.
        if row == GRID_SIZE:
            results.append(list(columns))
            return

        # RECURSIVE CASE: Try every column in this row
        for col in range(GRID_SIZE):
            if is_valid(row, col):
                columns[row] = col      # Make a choice
                place_queens(row + 1)   # Explore
                columns[row] = -1       # BACKTRACK: "Undo" the choice

    def is_valid(row, col):
        """Check if placing a queen at (row, col) is safe."""
        for prev_row in range(row):
            prev_col = columns[prev_row]
            
            # 1. Check same column
            if prev_col == col:
                return False
            
            # 2. Check diagonals
            # Distance between columns == distance between rows
            if abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    place_queens(0)
    return results

# Run the puzzle
solutions = solve_queens()
print(f"Found {len(solutions)} ways to place the queens!")
print(f"Example solution (Row mapping): {solutions}")