


def maxCoins(nums) -> int:
    t = [[-1]*(len(nums)+1)]*(len(nums)+1)  
    return solve(nums, 1, len(nums)-1, t)

def solve(nums, i, j, t):
    minimum = float("inf")
    if i == j:
        return 0
    if t[i][j] != -1:
        return t[i][j]
    for k in range(i, j):
        temp = solve(nums, i, k, t) + solve(nums, k+1, j, t) + (nums[i-1]*nums[k]*nums[j])
        minimum = min(temp, minimum)
    t[i][j] = minimum
    return t[i][j]


print(maxCoins([1, 2, 3, 4]))
