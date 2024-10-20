class Solution(object):
    def setZeroes(self, matrix):
        colZ = set()
        rowZ = set()
        m , n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rowZ.add(i)
                    colZ.add(j)
        for i in range(m):
            for j in range(n):
                if i in rowZ or j in colZ:
                    matrix[i][j]=0
        
                
                   
        
         