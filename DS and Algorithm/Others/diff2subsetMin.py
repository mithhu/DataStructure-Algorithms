wt = [1, 2, 7]


def partition(wt):
    wtSum = sum(wt)
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

    for i in reversed(range(len(t[-1]))):
        if t[-1][i] == True:
            return wtSum - (2*i)


print(partition(wt))
