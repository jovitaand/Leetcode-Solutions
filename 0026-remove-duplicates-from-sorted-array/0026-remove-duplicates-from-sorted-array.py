class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1: # while pointer less than length of array
            if nums[i]==nums[i+1]: # if duplicate is found
                del nums[i] # delete duplicate
            else:
                i = i+1 #increment
        return len(nums) #return the lenght of the array