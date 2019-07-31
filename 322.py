def coinChange(coins: list, amount: int) -> int:
    MAX = float('inf')
    dp = [0] + [MAX] * amount
    for i in range(1, amount+1):
        dp[i] = min([ dp[i-coin] if i-coin>=0 else MAX for coin in coins])+1
    return -1 if dp[-1] == float('inf') else dp[-1]

#Classic case of dynamic programing and counter example of greedy.
#dp[i] records the minimal coins needed to make up amount i. And it's one more coin than the minimum of dp[i-j] for j in coins.