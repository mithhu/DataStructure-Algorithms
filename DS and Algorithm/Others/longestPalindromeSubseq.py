def longestPalindromesequence(text1: str) -> int:
    text2 = text1[::-1]
    t = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]

    for i in range(1, len(text1)+1):
        for j in range(1, len(text2)+1):
            if text1[i-1] == text2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])
    return t[-1][-1]


print(longestPalindromesequence("agbcba"))
