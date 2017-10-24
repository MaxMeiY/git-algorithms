def print_interleaveings(str1, m, str2, n, output_str, i):
    if m == 0 and n == 0:
        to_str(output_str)

    if m != 0:
        output_str[i] = str1[0]
        print_interleaveings(str1[1:], m-1, str2, n, output_str, i+1)

    if n != 0:
        output_str[i] = str2[0]
        print_interleaveings(str1, m, str2[1:], n-1, output_str, i+1)

def to_str(List):
    print(''.join(List))
    return

def interleaving(str1, str2):
    m = len(str1)
    n = len(str2)
    output_str = [''] * (m+n)
    print_interleaveings(str1, m, str2, n, output_str,0)