# class Solution:
# @param A : string
# @return an integer


def cnttrue(A):
    n = len(A)
    T = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(2)]
    return Solve(T, A, 0, n-1, True)


def Solve(T, S, i, j, isTrue):
    if i > j:
        return False
    if i == j:
        if isTrue:
            return S[i] == 'T'
        else:
            return S[i] == 'F'
    if T[isTrue][i][j] != -1:
        return T[isTrue][i][j]
    count = 0
    for k in range(i+1, j, 2):
        LT = Solve(T, S, i, k-1, True)
        LF = Solve(T, S, i, k-1, False)
        RT = Solve(T, S, k+1, j, True)
        RF = Solve(T, S, k+1, j, False)

        if S[k] == '&':
            if isTrue:
                count = count + LT * RT
            else:
                count = count + LT * RF + LF * RT + LF * RF
        elif S[k] == '|':
            if isTrue:
                count = count + LT * RF + LF * RT + LT * RT
            else:
                count = count + LF * RF
        elif S[k] == '^':
            if isTrue:
                count = count + LT * RF + LF * RT
            else:
                count = count + LT * RT + LF * RF
        T[isTrue][i][j] = count
    return count


print(cnttrue("F|T^T&F"))
