class Solution(object):
    def findDuplicate(self, nums):
        d= collections.Counter(nums)
        for i in range(1, len(nums)+1):
            if d[i]>1:
                return i
                
        
        
        