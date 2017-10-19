def has_sum_of_2_nums_equal_to_x(array, x):
    '''
    given an array of nums and x, find two nums whose
    sum is equal to x.

    Time: O(nlg(n))
    constant extra memory
    '''
    length = len(array)
    quick_sort(array, 0, length-1)

    first = 0
    last = length -1
    temp = 0

    while first < last:
        if array[first] + array[last] == x:
            return array[first], array[last]
        elif array[first] + array[last] < x:
            first += 1
        else:
            last -= 1
    return False









def quick_sort(array, a, b):
    if a >= b:
        return
    pivot = array[b]
    left = a
    right = b - 1

    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1

        while left <= right and array[right] > pivot:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], \
                                        array[left]
    # place pivot at right place
    array[left], array[b] = array[b], array[left]

    # recursively sort the rest
    quick_sort(array, a, left-1)
    quick_sort(array, left+1, b)