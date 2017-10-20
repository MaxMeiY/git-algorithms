'''
page 119 
'''
def min_coins(coins, n, s):
    '''
    find minimum number of coins for a value of s
    '''

    # base condition
    if s == 0:
        return 0

    res = float("inf")
    for i in range(n):
        # try every coin that was < s
        if coins[i] <= s:
            temp = min_coins(coins, n, s-coins[i])

            if temp + 1 < res:
                res = temp + 1
    return res

def DP_min_coins(coins, n, s):
    '''
    DP version
    '''
    memo = [float("inf") for _ in range(s+1)]

    # if s == 0, result = 0
    memo[0] = 0

    # compute values botton-up
    for i in range(1, s+1):
        # go through all coins < i
        for j in range(len(coins)):
            if coins[j] <= i:
                temp = memo[i-coins[j]]
                if temp != float("inf") and \
                   temp + 1 < memo[i]:
                    memo[i] = temp + 1
    print(memo)
    return memo[s]