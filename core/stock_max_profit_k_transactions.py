def maxProfit(self, k: int, prices: List[int]) -> int:
    """
Best Time to Buy and Sell Stock with at most k transactions.

Given a list of daily prices, this algorithm computes the maximum achievable
profit using at most k buy–sell transactions. At any time, at most one stock
can be held.

We use a dynamic programming approach with the following state:

    dp[day][state][l]

where:
- day   ∈ {0, ..., n-1} is the current day,
- state ∈ {0, 1} indicates whether we are not holding (0) or holding (1) a stock,
- l     ∈ {0, ..., k-1} indexes the remaining available transactions.

The DP is computed backwards in time. Transitions model the choice between
holding, buying, or selling a stock, while respecting the transaction limit.

Time complexity:  O(n * k)
Space complexity: O(n * k)

This implementation focuses on clarity of state definition and transitions,
and is suitable as a reference solution for multi-dimensional dynamic
programming problems.
"""
    n=len(prices)
    k=min(k,n)
    dp=[[[0]*k for _ in range(2)] for j in range(n)]
    dp[n-1][1]=[prices[n-1]]*k
    for j in range(1,n):
        for l in range(k):
            dp[n-1-j][0][l]=max(dp[n-1-j+1][0][l],dp[n-1-j+1][1][l]-prices[n-1-j])
            if l!=k-1:
                dp[n-1-j][1][l]=max(dp[n-1-j+1][1][l],dp[n-1-j+1][0][l+1]+prices[n-1-j])
            else:
                dp[n-1-j][1][l]=max(dp[n-1-j+1][1][l],prices[n-1-j])
    return dp[0][0][0]
