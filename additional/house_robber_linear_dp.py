#exercise: https://leetcode.com/problems/house-robber/?envType=problem-list-v2&envId=dynamic-programming

def rob(self, nums: List[int]) -> int:
    ''' this function return the optimal
    strategy for a thief who wants to rob houses
    containing nums[i] gold under the constraint 
    that no adjoint houses can be robbed.
    It returns the maximum gold obtainable.
    space complexity: O(len(nums))
    time complexity: O(len(nums))
    '''
    n=len(nums)
    if n<=2:
        return max(nums)
    left=[0]*(n+1) #left[j]=starting robbing at house j
    left[n-1]=nums[n-1]
    for j in range(1,n):
        left[n-1-j]=max(nums[n-1-j]+left[n-1-j+2],left[n-1-j+1])
    return left[0]
