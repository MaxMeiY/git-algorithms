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
