def lcs(str1, str2, m, n):
    if m == 0 or n == 0:
        return 0
    
    if str1[m-1] == str2[n-1]:
        return 1 + lcs(str1,str2,m-1,n-1)

    else:
        return max(lcs(str1,str2,m-1,n),
                   lcs(str1,str2,m, n-1))

def DP_lcs(str1, str2, m, n):
    memo = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i][j-1],
                                 memo[i-1][j])
    return memo,memo[i][j]

def prin_lcs(str1, str2):
    m, n = len(str1), len(str2)
    memo, length = DP_lcs(str1,str2,m,n)
    result = []

    while m > 0 and n > 0:
        if length == 0:
            return

        # if current char in str1 and str2 equal,
        # then it is part of LCS
        if str1[m-1] == str2[n-1]:
            result.append(str1[m-1])
            m, n, length = m-1,n-1, length-1
        elif memo[m-1][n] > memo[m][n-1]:
            m -= 1
        else:
            n -= 1
    return ''.join(reversed(result))

