class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            if nums[i-1] > 0: #removing all of the negative signs
                nums[i] = nums[i] + nums[i-1] #adding the postive integer sum
        ans = max(nums)
        return ans
        
        
        
        
        