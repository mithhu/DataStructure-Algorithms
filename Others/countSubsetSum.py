wt = [1, 2, 3, 3]
W = 6
n = len(wt)


def subsetSum(W, wt, n):
    t = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                t[i][j] = t[i-1][j-wt[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[-1][-1]


print(subsetSum(W, wt, n))
