'''
see page 89
'''

def edit_distance(str1, str2):
    string1 = list(str1)
    string2 = list(str2)
    return _calculate_distance(string1, 0, string2, 0)

def _calculate_distance(str1, m, str2, n):
    # if str1 is empty,
    # then all characters of str2 need to inserted
    if str1[m:] == []:
        return len(str2) - n

    # if str2 is empty
    # then all characters of str1 need to be deleted
    if str2[n:] == []:
        return len(str1) - m

    # if first characters of both are same
    # then ignore it and find edit distance
    # of rest of the strings
    if str1[m] == str2[n]:
        return _calculate_distance(str1, m+1, str2, n+1)

    # find edit distance for all three operations
    i = _calculate_distance(str1, m, str2, n+1)
    d = _calculate_distance(str1, m+1, str2, n)
    u = _calculate_distance(str1, m+1, str2, n+1)

    return min(i, d, u) + 1


def DP_edit_distance(str1, str2):
    string1 = list(str1)
    string2 = list(str2)
    return _DP_edit_distance(string1, string2)

def _DP_edit_distance(list_str1, list_str2):
    m = len(list_str1)
    n = len(list_str2)
    memo = [[i for i in range(m+1)] for _ in range(n+1)]
    for j in range(1, n+1):
        for i in range(1, m+1):
            if list_str1[i-1] == list_str2[j-1]:
                memo[j][i] = memo[j-1][i-1]
            else:
                memo[j][i] = 1 + min(memo[j-1][i-1],
                                     memo[j][i-1],
                                     memo[j-1][i])
    return memo[n][m]