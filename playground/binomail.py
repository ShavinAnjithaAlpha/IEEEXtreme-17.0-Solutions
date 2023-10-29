def binomial_coefficient(n, k):
    # Initialize a 2D array to store the binomial coefficients
    dp = [[0 for j in range(k+1)] for i in range(n+1)]

    # Base case: C(n, 0) = 1
    for i in range(n+1):
        dp[i][0] = 1

    # Base case: C(n, n) = 1
    for i in range(1, n+1):
        dp[i][i] = 1

    # Fill in the rest of the table using dynamic programming
    for i in range(1, n+1):
        for j in range(1, k+1):
            # Use previously calculated values to compute the current value
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    print(dp)

    # Return the binomial coefficient
    return dp[n][k]


binomial_coefficient(5, 2)
