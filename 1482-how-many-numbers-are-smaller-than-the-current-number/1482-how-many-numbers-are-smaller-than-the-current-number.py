class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i = 0 
        count = 0  
        result = []
        while i<len(nums):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count+=1
            result.append(count)
            count = 0
            i+=1
        return result