class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        if n == 0 or n % 4!= 0:
            return False
        n=n//4
        return self.isPowerOfFour(n)
        