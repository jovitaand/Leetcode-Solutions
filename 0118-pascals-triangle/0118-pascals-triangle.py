class Solution(object):
    def generate(self, numRows):
        f = [1,1]
        
        for i in range(2,numRows):
            f.append(f[i-1]*i)
			
        # General Pascal's Triangle 
        return [[int(f[r]/(f[c] * f[r-c])) for c in range(r+1)] for r in range(numRows)]