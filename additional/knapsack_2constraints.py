def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    '''
    knapsack 0/1 problem with 2 constraints.
    Given strs a list of strings formed only by 0's and 1's
    this function return the maximum dimension of a subset 
    of strs containing in total at most m 0's and n 1's.
    We use a 2D dinamical programming approach by saving in 
    dp[s][k] the optimal strategy of choosing elements by having
    at most s 1's and k 0's. by iterating over the elemet of strs
    and filling the matrix backward (i.e. starting from dp[n][m] 
    and going towards dp[0][0]) we decide for every element of
    strs wheter if it is better to take it or leave it. Filling
    backwards avoid multiple choice of the same element.
    Space complexity: O(m*n)
    Time complexity: O( sum_{s in strs} |s| + len(strs) * m * n )
    
    The first term accounts for counting zeros and ones in each string,
    while the second term corresponds to the dynamic programming update.
    '''
    len_strs=len(strs)
    dp=[[0]*(m+1) for _ in range(n+1)]
    ones=strs[len_strs-1].count('1')
    zeros=len(strs[len_strs-1])-ones
    for k in range(zeros,m+1):
        for s in range(ones,n+1):
            dp[s][k]=1
    for l in range(1,len(strs)):
        ones=strs[len_strs-1-l].count('1')
        zeros=len(strs[len_strs-1-l])-ones
        for k in range(m,-1,-1):
            for s in range(n,-1,-1):
                if k>=zeros and s>=ones:
                    dp[s][k]=max(dp[s-ones][k-zeros]+1,dp[s][k])
    return dp[n][m]
