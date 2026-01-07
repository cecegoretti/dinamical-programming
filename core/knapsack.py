def optimalfilling(values, weights, max_weight):
  """
    0/1 Knapsack problem.

    dp[i][w] = maximum total value using the first i items
               with knapsack capacity w.

    Time complexity: O(n * W)
    Space complexity: O(n * W)
    """
    dp=[[0]*len(values) for _ in range(max_weight+1)]
    #dp[j][i] saves the optimal filling with maximal capacity j using the first i elements
    for j in range(max_weight+1):
        if weights[0]<=j:
            dp[j][0]=values[0]
    for i in range(1,len(values)):
        for j in range(max_weight+1):
            if weights[i]<=j:
                dp[j][i]=max(dp[j-weights[i]][i-1]+values[i],dp[j][i-1])
            else:
                dp[j][i]=dp[j][i-1]
    return dp[max_weight][len(values)-1]
