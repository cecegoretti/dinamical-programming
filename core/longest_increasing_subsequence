#compute the lenght of the longest increasing subsequence (not substring)
#leetcode exercise: https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=problem-list-v2&envId=dynamic-programming
#dp[i] saves the lenght of the longest increasing subsequence ending in position i
#memory used: len(nums), time complexity: len(nums)**2

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
