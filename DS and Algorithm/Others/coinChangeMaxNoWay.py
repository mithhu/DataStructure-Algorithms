class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row = amount + 1
        column = len(coins) + 1
        K = [[-1 for x in range(row)] for y in range(column)]
        for i in range(row):
            K[0][i] = 0
        for i in range(column):
            K[i][0] = 1
        for i in range(1, column):
            for j in range(1, row):
                if(coins[i-1] <= j):
                    K[i][j] = K[i-1][j] + K[i][j - coins[i-1]]
                else:
                    K[i][j] = K[i-1][j]
        return K[-1][-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0 for price in range(amount+1)]
        ways[0] = 1
        for denom in coins:
            for price in range(1, amount+1):
                if denom <= price:
                    ways[price] += ways[price - denom]
        return ways[amount]
