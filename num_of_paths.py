'''
<Dynamic programming for coding interviews>
page 91
'''


# count from 1.
def num_of_paths(m, n):
    if m == 1 and n == 1: # CELL (1, 1)
        return 0
    if m == 1 or n == 1:  # first row or left column
        return 1

    return num_of_paths(m-1, n) + num_of_paths(m, n-1)

# count from 0
def DP_num_of_paths(m, n):
    memo = [[1 for _ in range(n)] for _ in range(m)]
    memo[0][0] = 0

    for i in range(1, m):
        for j in range(1, n):
            memo[i][j] = memo[i-1][j] + memo[i][j-1]
    return memo[m-1][n-1]