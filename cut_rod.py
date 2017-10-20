'''
page 121
'''
def cut_rod(values, l):
    '''
    value array holds the market value of each length
    l is total length of the rod
    '''
    if l <= 0:
        return 0
    max_value = float("-inf")

    # try every length
    for i in range(1, l+1):
        max_value = max(max_value,
                        values[i-1] + cut_rod(values,l-i))

    return max_value


def DP_cut_rod(values, l):
    memo = [float("-inf") for _ in range(l+1)]
    memo[0] = 0

    # calculate values from 1 to l
    for i in range(1, l+1):
        # try every length
        for j in range(i):
            memo[i] = max(memo[i], values[j]+memo[i-j-1])

    return memo[l]

if __name__ == '__main__':
    values = [1,5,8,9,10,17,17,20]
    print(cut_rod(values, 4))
    print(DP_cut_rod(values, 4))