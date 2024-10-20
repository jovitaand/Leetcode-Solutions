class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n == 0 or n % 2 != 0:
            return False
        n = n//2
        return self.isPowerOfTwo(n)
        