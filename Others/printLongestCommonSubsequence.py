def printLongestCommonSubsequence(text1: str, text2: str) -> int:
    t = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]

    for i in range(1, len(text1)+1):
        for j in range(1, len(text2)+1):
            if text1[i-1] == text2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])

    index = t[i][j]
    print(index)
    lcs = [""]*(index)

    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs[index-1] = text1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif t[i-1][j] > t[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


print(printLongestCommonSubsequence("abcde", "bcdfe"))
