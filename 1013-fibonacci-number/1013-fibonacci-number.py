class Solution(object):
    def fib(self, n):
        n1, n2 = 0, 1
    	for i in range(1,n+1): 
            n1, n2 = n2, n1 + n2
    	return n1
        
            
        