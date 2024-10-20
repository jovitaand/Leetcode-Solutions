class Solution(object):
    def singleNumber(self, nums):
        xor=0 
        for num in nums:
            xor ^= num
        return xor 
    #returns 1 if it occurs once
        
             
   