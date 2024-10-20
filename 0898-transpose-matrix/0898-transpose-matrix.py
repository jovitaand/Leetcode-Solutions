class Solution(object):
    def transpose(self, matrix):
        return (zip(*matrix))
         
        #How it works: zip(*a) is equal to zip(a[0], a[1], a[2]).