'''
page 125 
'''

def knapsack(c, weight, value, n):
    '''
    weight[n]; // weight array
    value[n]; // value array
    n items
    c total weight that can be carried
    '''
    # total weight that can carried is <= 0 or
    # there are no items left (<= 0)
    if c <= 0 or n <= 0:
        return 0

    # for those items > c, discrad it
    if weight[n-1] > c:
        return knapsack(c, weight, value, n-1)

    # include this item
    x = value[n-1] + knapsack(c-weight[n-1], weight,
                              value, n-1)

    # not include this item
    y = knapsack(c, weight, value, n-1)

    return max(x, y)

def DP_knapsack(c, weight, value, n):
    # init table, top row and first col should be 0
    table = [[0 for _ in range(c+1)] for _ in range(n+1)]

    # every item up to n
    for i in range(1, n+1):
        # every capacity up to c
        for j in range(1, c+1):
            # two cases: weight[i-1] >= j. or else
            if weight[i-1] <= j:
                # if add this weight, cal the remaining c
                x = j - weight[i-1]
                table[i][j] = max(value[i-1] + \
                                  table[i-1][x],
                                  table[i-1][j])
            else:
                table[i][j] = table[i-1][j]

    print_items(n, c, weight, value, table)
    return table[n][c]

def print_items(n, c, weight, value, table):
    result = []
    while n > 0:
        if table[n][c] == table[n-1][c]:
            n -= 1
        elif c >= weight[n-1]:
            print((n,c))
            result.append((n, value[n-1]))
            c = c - weight[n-1]
            n -= 1
    print(result)

if __name__ == '__main__':
    weight = [2,3,4,5]
    value = [3,4,5,6]

    print(DP_knapsack(7, weight, value, 4))