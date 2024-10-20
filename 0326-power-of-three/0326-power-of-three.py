class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        if n == 0 or n%3 != 0:
            return False
        n = n//3 # checking its divisbility
        return self.isPowerOfThree(n) # using recursion
         