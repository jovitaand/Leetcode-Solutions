class Solution(object):
    def pivotIndex(self, nums):
        lsum = 0
        total = sum(nums)
        for indx in range(len(nums)):
            rsum = total - nums[indx] - lsum
            if lsum == rsum:
                return indx
            lsum += nums[indx]
        return -1
            
        