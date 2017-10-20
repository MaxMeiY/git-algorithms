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
    print(memo)

    max_length = memo[0]
    for i in range(1,len(array)):
        if memo[i] > max_length:
            max_length = memo[i]
    return max_length
