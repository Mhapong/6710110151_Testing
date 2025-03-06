def gridChallenge(grid):
    rows = len(grid)
    if rows == 0:
        return "YES"

    cols = len(grid[0])
    if any(len(row) != cols for row in grid):
        return "NO"

    sorted_grid = ["".join(sorted(row)) for row in grid]

    for j in range(cols):
        for i in range(rows - 1):
            if sorted_grid[i][j] > sorted_grid[i + 1][j]:
                return "NO"

    return "YES"