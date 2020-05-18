wt = [2, 3, 5, 7]
W = 11
n = len(wt)


def subsetSum(W, wt, n):
    t = [[False for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                t[i][j] = t[i-1][j-wt[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[-1][-1]


print(subsetSum(W, wt, n))
