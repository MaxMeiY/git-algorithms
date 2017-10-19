'''
see page 106
worth seeing
'''

def subset_sum(array, i, len_of_array, x):
    '''
    Input array: {3, 2, 7, 1}  x = 6
    Output: True // in that sum of ele of {3, 2, 1} is 6
    '''
    # base case
    if x == 0:
        return True

    # tried all eles
    if len_of_array == 0:
        return False

    # ignore it
    if array[i] > x:
        return subset_sum(array, i+1, len_of_array-1, x)

    # else, tried including array[i], and not including
    # array[i]

    return subset_sum(array, i+1, len_of_array-1, x) or \
        subset_sum(array, i+1, len_of_array-1, x - array[i])


def DP_subset_sum(array, n, x):
    '''
    The value of memo[i][j] is true if there is a
    memo of arr[0..j] with x equal to j
    '''
    memo = [[None for i in range(n + 1)] for _ in range(x+1)]

    # if x is 0, then answer is true
    for i in range(n):
        memo[0][i] = True

    # if x is not 0 and array is empty, answer is false
    for i in range(1, x+1):
        memo[i][0] = False

    # fill the memo table in botton up answer
    for i in range(1, x+1):
        for j in range(1, n+1):
            memo[i][j] = memo[i][j-1]
            if i >= array[j-1]:
                memo[i][j] = memo[i][j]  or \
                             memo[i - array[j-1]][j-1]

    if memo[x][n]:
        return print_subset(array, memo, x, n, x)

    else:
        return False

def print_subset(array, memo, row, col, x):
    result_list = []
    while x != 0:
        if memo[row][col-1] is False:
            result_list.append(array[col-1])
            x = x - array[col-1]
            row = row - array[col-1]
            col -= 1
        else:
            col -= 1
    return result_list

