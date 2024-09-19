def print_grid(grid):
    """Helper function to print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) for num in row))


def is_valid_move(grid, row, col, num):
    """Check if placing 'num' in grid[row][col] is valid."""
    # Check the row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check the 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[box_row_start + i][box_col_start + j] == num:
                return False

    return True


def find_empty_location(grid):
    """Find an empty cell in the grid. Returns (row, col) or None if no empty cell exists."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:  # 0 represents an empty cell
                return (i, j)
    return None


def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True  # Puzzle solved
    row, col = empty_loc

    for num in range(1, 10):  # Numbers 1-9
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num  # Place the number

            if solve_sudoku(grid):  # Recursively attempt to solve
                return True

            # If placing num didn't lead to a solution, reset and try next number
            grid[row][col] = 0

    return False  # Trigger backtracking


# Example Sudoku puzzle (0s represent empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

if solve_sudoku(sudoku_grid):
    print("Solved Sudoku Grid:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
