


def maxCoins(str) -> int:
    n = len(str)  
    t = [[-1 for _ in range(n)] for _ in range(n)]

    return solve(str, 0, len(str)-1, t)

def isPalindrome(string, leftidx, rightIdx):
    while leftidx < rightIdx:
        if string[leftidx] != string[rightIdx]:
            return False
        leftidx += 1
        rightIdx -= 1
    return True

def solve(str, i, j, t):
    minimum = float("inf")
    if i >= j:
        return 0
    if isPalindrome(str, i, j):
        return 0
    if t[i][j] != -1:
        return t[i][j]
    for k in range(i, j):
        temp = 1 + solve(str, i, k, t) + solve(str, k+1, j, t)
        # minimum = min(temp, minimum)
        if temp < minimum: 
            minimum = temp
    t[i][j] = minimum
    return t[i][j]


print(maxCoins("coder"))

