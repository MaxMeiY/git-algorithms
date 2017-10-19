'''
page 100
'''

def is_interleaved(str1, str2, str3):
    '''
    str3 is said to be interleaving of str1 and str2 if
    it contains all the characters of str1 and str2 and
    the relative order of characters of both strings
    is preseved in str3.

    Input: str1:'xyz' str2:'abcd' str3:'xabyczd'
    Output: True
    '''

    m = len(str1)
    n = len(str2)

    # str3 should have exactly m + n characters
    if len(str3) != m + n:
        return False

    # 2-Dim Array
    memo = [[True for _ in range(n+1)] for _ in range(m+1)]

    # populating first column
    for i in range(1, m+1):
        if str1[i-1] != str3[i-1]:
            memo[i][0] = False
        else:
            memo[i][0] = memo[i-1][0]

    # populating first row
    for j in range(1, n+1):
        if str2[j-1] != str3[j-1]:
            memo[0][j] = False
        else:
            memo[0][j] = memo[0][j-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] != str3[i+j-1] and \
               str2[j-1] != str3[i+j-1]:
                memo[i][j] = False

            elif str1[i-1] == str3[i+j-1] and \
                 str2[j-1] != str3[i+j-1]:
                memo[i][j] = memo[i-1][j]

            elif str1[i-1] != str3[i+j-1] and \
                 str2[j-1] != str3[i+j-1]:
                memo[i][j] = memo[i][j-1]

            # both equal
            else:
                memo[i][j] = (memo[i-1][j] or \
                              memo[i][j-1])
    return memo[m][n]
