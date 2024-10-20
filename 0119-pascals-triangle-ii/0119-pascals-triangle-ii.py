import math
class Solution(object): 
    def getRow(self, rowIndex):
        ans=[]
        n=rowIndex
        for i in range( n+1):
            ans.append(int(math.factorial(n)/(math.factorial(n-i)*math.factorial(i))))
        return ans
    #the pascals triangle is equal to permutation ncr in every position
        

      
        