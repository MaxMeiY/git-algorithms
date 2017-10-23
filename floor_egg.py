'''
page 134
'''
memo = [[False for _ in range(11)] for _ in range(101)]


def drop_eggs(num_floors, num_eggs):

    # if num_floors == 0 or 1, there's only 0 or 1 try
    # if num_eggs == 1, try is linear, so num_floors tries
    if memo[num_floors][num_eggs] is not False:
        return memo[num_floors][num_eggs]

    if num_floors == 0 or num_floors == 1 or num_eggs == 1:
        return num_floors

    minimum = float('inf')

    for floor in range(1, num_floors+1):

        # two cases:
        # if break, start up to floor - 1, eggs - 1
        # if not, search remaining floors, eggs the same
        temp = max(drop_eggs(floor-1, num_eggs-1),
                   drop_eggs(num_floors-floor, num_eggs))
        if temp < minimum:
            minimum = temp
    memo[num_floors][num_eggs] = minimum+1

    return memo[num_floors][num_eggs]


def DP_drop_eggs(num_floors, num_eggs):
    memo = [[0 for _ in range(num_eggs+1)] for _ in range(num_floors+1)]
    for i in range(1, num_floors+1):
        memo[i][1] = i

    temp = 0
    for i in range(1, num_floors+1):
        for j in range(2, num_eggs+1):
            memo[i][j] = float("inf")
            for k in range(1, i+1):
                temp = 1 + max(memo[k-1][j-1],
                               memo[i-k][j])
                if temp < memo[i][j]:
                    memo[i][j] = temp
    return memo[num_floors][num_eggs]
