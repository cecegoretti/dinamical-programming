#leetcode exercise: https://leetcode.com/problems/distinct-subsequences/?envType=problem-list-v2&envId=dynamic-programming

def numDistinct(self, s: str, t: str) -> int:
    """
    Count the number of distinct subsequences of s that equal t.
    
    DP approach:
    dp[i][j] = number of subsequences of s[:j] equal to t[:i]

    Time complexity: O(len(s) * len(t))
    Space complexity: O(len(s) * len(t))
    """
    dp=[[0]*(len(s)+1) for J in range(len(t)+1)]
    if len(t)==1:
        return s.count(t)
    for j in range(1,len(s)+1): 
        dp[1][j]=s[:j].count(t[0])
    for i in range(2,len(t)+1): 
        for j in range(i,len(s)+1):
            if t[i-1]==s[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
            else:
                dp[i][j]=dp[i][j-1]
    return dp[len(t)][len(s)]
