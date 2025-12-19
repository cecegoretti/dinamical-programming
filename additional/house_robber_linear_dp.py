#How to optimally rob houses given the money in each house of the street given by the array nums and that no two adjacent house can be robbes
#leetcode exercise: https://leetcode.com/problems/house-robber/?envType=problem-list-v2&envId=dynamic-programming
#memory used: len(nums)= number of houses, time complexity: len(nums)



class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return max(nums)
        left=[0]*(n+1) #left[j]=starting robbing at house j
        left[n-1]=nums[n-1]
        for j in range(1,n):
            left[n-1-j]=max(nums[n-1-j]+left[n-1-j+2],left[n-1-j+1])
        return left[0]
