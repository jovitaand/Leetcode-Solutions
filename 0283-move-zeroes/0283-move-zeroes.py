class Solution(object):
    def moveZeroes(self, nums):
          for number in nums:
                if number == 0:
                    nums.append(nums.pop(nums.index(0)))