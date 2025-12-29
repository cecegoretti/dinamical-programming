#exercise:https://leetcode.com/problems/decode-ways-ii/description/
#time complexity: O(len(s))
#space complexity: O(len(s)) (can be optimized to O(1))
def numDecodings(self, s: str) -> int:
    ''' This function decode a string s containing numbers and *.
        Each number from 1 to 26 can encode an alphabet letter.
        * can replace any digit from 1 to 9.
        The function trace back the value by computing the number
        of possible decodes of the tail of s. This is done by studying
        the cases of possible combination of adjacent element in s.
    '''
    n=len(s)
    dp=[0]*(n+1)
    dp[n]=1
    if s[n-1]!='0':
        if s[n-1]!='*':
            dp[n-1]=1
        else:
            dp[n-1]=9
    for j in range(1,n-1+1):
        if s[n-1-j]!='0':
            if s[n-1-j]!='*' and s[n-1-j+1]!='*':
                if int(s[n-1-j]+s[n-1-j+1])<=26:
                    dp[n-1-j]=dp[n-1-j+2]+dp[n-1-j+1]
                else:
                    dp[n-1-j]=dp[n-1-j+1]
            elif s[n-1-j]!='*' and s[n-1-j+1]=='*':
                if int(s[n-1-j])<=2:
                    if s[n-1-j]=='1':
                        dp[n-1-j]=dp[n-1-j+1]+9*dp[n-1-j+2]
                    else:
                        dp[n-1-j]=dp[n-1-j+1]+6*dp[n-1-j+2]
                else:
                    dp[n-1-j]=dp[n-1-j+1]
            elif s[n-1-j]=='*' and s[n-1-j+1]!='*':
                if int(s[n-1-j+1])<=6:
                    dp[n-1-j]=9*dp[n-1-j+1]+2*dp[n-1-j+2]
                else:
                    dp[n-1-j]=9*dp[n-1-j+1]+dp[n-1-j+2]
            else:
                dp[n-1-j]=9*dp[n-1-j+1]+15*dp[n-1-j+2]
            dp[n-1-j]=dp[n-1-j]%(10**9+7)
    return dp[0]%(10**9+7)
