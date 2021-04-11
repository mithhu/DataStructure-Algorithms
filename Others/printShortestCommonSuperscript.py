def shortestCommonSupersequence(str1: str, str2: str) -> str:
    t = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])

    scs = ""

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            scs += str1[i-1]
            # index -= 1
            i -= 1
            j -= 1
        elif t[i-1][j] > t[i][j-1]:
            scs += str1[i-1]
            # index -= 1
            i -= 1
        else:
            scs += str2[j-1]
            # index -= 1
            j -= 1
    while i > 0:
        scs += str1[i-1]
        # index -= 1
        i -= 1
    while j > 0:
        scs += str2[j-1]
        # index -= 1
        j -= 1
    return scs


print(shortestCommonSupersequence("abac", "cab"))
