exercise: https://leetcode.com/problems/combination-sum-iv/

def combinationSum4(self, nums: List[int], target: int) -> int:
'''  
  This function computes in how many different ways
  one can obtain the value amount by adding elements of nums.
  Sequences that differ in the order are counted
  as different.
  Space complexity: O(len(nums))
  Time complexity: O(len(nums)*target)
'''
  n=len(nums)
  dp=[0]*(target+1)
  dp[0]=1
  for x in range(target+1):
    for c in nums:
      if x-c>=0:
        dp[x]+=dp[x-c]
  return dp[target]
