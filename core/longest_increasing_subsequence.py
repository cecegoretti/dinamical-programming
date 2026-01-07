def lengthOfLIS(self, nums: List[int]) -> int:
    '''
    Compute the lenght of the longest increasing subsequence (not substring)
    of nums. 
    It uses a dinamical programming approach:
    dp[i] saves the lenght of the longest increasing 
    subsequence ending in position i.
    
    Space complexity: O(len(nums))
    Time complexity: O(len(nums)**2)
    '''
    dp = [1] * len(nums)
    for j in range(1, len(nums)):
        for i in range(j):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    return max(dp)
