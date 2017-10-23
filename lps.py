'''
page 128.
Longest Palindromic Subsequence
Such that 'BBABCBCAB'
return 7 cause BABCBAB is the longest subsequence that is
a palindrome
'''

def lps(string, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if string[start] == string[end]:
        return 2 + lps(string, start+1, end-1)
    else:
        return max(lps(string, start+1, end),
            lps(string, start, end-1))

def DP_lps(string, n):

    # single str is palindrome of length 1
    # therefore initializing with 1
    table = [[1 for _ in range(n)] for _ in range(n)]

    # k is each step, from 2 to n
    for k in range(2, n+1):
        # i is start of each step
        for i in range(0, n-k+1):
            # j is end of each step
            j = i + k - 1
            if string[i] == string[j] and k == 2:
                table[i][j] = 2
            elif string[i] == string[j]:
                table[i][j] = table[i+1][j-1] + 2
            else:
                table[i][j] = max(table[i][j-1], \
                                  table[i+1][j])
    for i in range(n):
        print(table[i])
    return table[0][n-1]