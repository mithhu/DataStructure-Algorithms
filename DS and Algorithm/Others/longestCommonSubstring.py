def findLength(A, B) -> int:
    maxlen, prev = 0, [0] * (len(B)+1)
    for i in range(1, len(A)+1):
        curr = [0] * (len(B)+1)
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                curr[j] = prev[j-1] + 1
                maxlen = max(maxlen, curr[j])

        prev = curr

    return maxlen


print(findLength("abcdef", "abcdfg"))
