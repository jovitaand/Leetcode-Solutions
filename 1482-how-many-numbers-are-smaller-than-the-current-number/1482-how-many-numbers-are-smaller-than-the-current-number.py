class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        result = []
        temp = sorted(nums)
        for i, num in enumerate(temp):
            if num not in d:
                d[num] = i
        for i in nums:
            result.append(d[i])
        return result 