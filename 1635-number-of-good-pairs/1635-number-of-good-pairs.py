class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i < j and nums[i]==nums[j]:
                    num.append([i,j])
        return len(num)
        
        
 