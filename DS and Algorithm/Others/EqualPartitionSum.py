wt = [1, 5, 11, 5]


def partition(wt):
    wtSum = sum(wt)
    if wtSum % 2 != 0:
        return False
    W = int(wtSum / 2)
    n = len(wt)
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


print(partition(wt))
