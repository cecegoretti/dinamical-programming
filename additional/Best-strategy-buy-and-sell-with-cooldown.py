def maxProfit(self, prices: List[int]) -> int:
    ''' given an array prices, such that prices[i] 
        indicates the price of a stock at day i, the 
        function computes the best strategy to optimize
        the profit by trading with the market knowing that
        after selling you can not buy the day after.
        The function simulates a three state machine, 
        the states are:
        -you can buy the stock;
        -you can sell the stock;
        -you must wait since you sold the day before.
        time and space complexity: O(n), n=len(prices).
        '''
    if len(prices)==1:
        return 0
    n=len(prices)
    dp=[[0,0,0] for _ in range(n)]
    #dp saves three possible states:
    #if we are ready to buy a stock, if 
    #we have already bought a stock or 
    #if we are waiting to buy a stock
    dp[n-1][1]=prices[n-1]
    for j in range(1,n):
        dp[n-1-j][0]=max(dp[n-1-j+1][0],dp[n-1-j+1][1]-prices[n-1-j])
        dp[n-1-j][1]=max(dp[n-1-j+1][2]+prices[n-1-j],dp[n-1-j+1][1])
        dp[n-1-j][2]=dp[n-1-j+1][0]
    return dp[0][0]
