'''
page 115 Question 9.9
'''

def length_of_longest_increasing_subsequence(array):
    '''
    Given an array of integers, return length of the
    longest increasing subsequence in the array
    '''
    memo = [1 for _ in range(len(array))]

    for i in range(1,len(array)):
        # increasing
        if array[i] > array[i-1]:
            memo[i] = memo[i-1] + 1
        else:
            memo[i] = 1

    max_length = memo[0]
    max_index = 0
    for i in range(1,len(array)):
        if memo[i] > max_length:
            max_length = memo[i]
            max_index = i
    print_sub_eles(array, max_index, max_length)


def print_sub_eles(array, max_index, max_length):
    result = []
    while max_length != 0:
        result.append(array[max_index])
        max_index, max_length = max_index-1, max_length-1
    print(result)
