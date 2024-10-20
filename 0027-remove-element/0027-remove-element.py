class Solution(object):
    def removeElement(self, nums, val):
        c = nums.count(val) #checking how many times val is repeated in nums
        for i in range(c): #iterating only no. of times c is repeated
            nums.remove(val) #removes the element
        return len(nums) 
    
    
    