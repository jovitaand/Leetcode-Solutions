class Solution(object):
    def hammingWeight(self, n):
         return str(bin(n)).count('1')
    #force the element into string -> convert it to binary -> counts 1 for all 