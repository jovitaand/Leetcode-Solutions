class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        completeList = list(range(len(nums)+1)) #generating the length of the list
        return sum(completeList)-sum(nums) #subtracting the length with sum of the list
        
                           