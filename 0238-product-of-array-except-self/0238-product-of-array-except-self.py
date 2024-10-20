class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n # [1] as the output array needs to store this in different stages as an element in the error

        #first left side:

        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
            
        #second right side:
        right_product = 1
        for i in range(n -1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output