T = int(input())


def max_path_grid(grid, K, B):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    # Create a 2D DP array to store the maximum path sums
    dp = [[0] * cols for _ in range(rows)]

    # Create a 2D array to track the consecutive blocks
    consecutive_blocks = [[0] * cols for _ in range(rows)]

    # Initialize the first cell with the grid's value
    dp[0][0] = grid[0][0]
    consecutive_blocks[0][0] = 1 if grid[0][0] < B else 0

    # Fill the first row and the first column
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
        consecutive_blocks[0][j] = consecutive_blocks[0][j -
                                                         1] + 1 if grid[0][j] < B else 0

    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        consecutive_blocks[i][0] = consecutive_blocks[i -
                                                      1][0] + 1 if grid[i][0] < B else 0

    # Fill the rest of the DP array
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

            if grid[i][j] < B:
                consecutive_blocks[i][j] = consecutive_blocks[i - 1][j] + 1
            else:
                consecutive_blocks[i][j] = 0

            if consecutive_blocks[i][j] > K:
                # dp[i][j] -= grid[i][j]
                return -1

    # The last cell (bottom-right corner) contains the maximum path sum
    return dp[rows - 1][cols - 1]


for i in range(T):
    (N, M, B, K) = tuple(map(int, input().split(" ")))
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split(" "))))

    val = max_path_grid(grid, K, B)
    if val == -1:
        print(f"Case {i+  1}: Impossible")
    else:
        print(f"Case {i+  1}: {max_path_grid(grid, K, B)}")
