COST = [[1, 4, 9, 17],
        [5, 6, 7, 14],
        [9, 9, 9, 12]]
COST2 = [[1, 3, 5, 8],
         [4, 2, 1, 7],
         [4, 3, 2, 3]]
         

MEN = [[0 for _ in range(4)] for _ in range(3)]

def min_path_cost(cost):
    MEN[0][0] = cost[0][0]

    # top row
    for i in range(1, 4):
        MEN[0][i] = MEN[0][i-1] + cost[0][i]

    # left column
    for i in range(1, 3):
        MEN[i][0] = MEN[i-1][0] + cost[i][0]

    for i in range(1, 3):
        for j in range(1, 4):
            MEN[i][j] = min(MEN[i-1][j], MEN[i][j-1]) + \
                        cost[i][j]
    return MEN[2][3]

def three_way_min_path(cost):
    MEN[0][0] = cost[0][0]

    # top row
    for i in range(1, 4):
        MEN[0][i] = MEN[0][i-1] + cost[0][i]

    # left column
    for i in range(1, 3):
        MEN[i][0] = MEN[i-1][0] + cost[i][0]

    for i in range(1, 3):
        for j in range(1, 4):
            MEN[i][j] = min(MEN[i-1][j],
                            MEN[i][j-1],
                            MEN[i-1][j-1]) + cost[i][j]
    return MEN[2][3]