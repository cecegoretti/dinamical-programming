#return the longest palindromic substring of s
#leetcode exercise: https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=dynamic-programming
#emory used: O(len(s)**2), time complexity: O(len(s)**2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[0]*len(s) for j in range(len(s))] #dp[j][i]=computes if the substring from j to i is palindrome
        for j in range(len(s)):
            dp[j][j]=1
        for j in range(len(s)-1):
            dp[j][j+1]=int(s[j]==s[j+1])
        for j in range(2,len(s)):
            for k in range(len(s)-j):
                dp[k][k+j]=int(s[k]==s[k+j])*dp[k+1][k+j-1]
        secret_word=""
        #secret_word stores the longest palindromic substring
        for j in range(len(s)):
            for k in range(j,len(s)):
                if dp[j][k]==1 and k-j+1>len(secret_word):
                    secret_word=s[j:k+1]
        #clearly this for cycle can be optimized by started looking from the longest possible substrings and going 
        #toward the shortest, if a palindromic substring is find the cycle stops. For clarity in reading we chose the slowest but 
        #clearest approach
        return secret_word
