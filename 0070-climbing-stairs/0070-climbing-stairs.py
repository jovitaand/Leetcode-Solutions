class Solution(object):
    def climbStairs(self, n):
        n1 , n2 = 0 ,1
        for i in range(0, n+1):
            n1, n2 = n2, n1+n2
        return n1 #similar to fibonacci series