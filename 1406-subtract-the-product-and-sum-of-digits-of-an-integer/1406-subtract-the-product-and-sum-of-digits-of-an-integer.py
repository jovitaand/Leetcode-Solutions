import numpy as np
class Solution(object):
    def subtractProductAndSum(self, n):
        
        x = [int(i) for i in str(n)]
        return np.prod(x) - np.sum(x)
