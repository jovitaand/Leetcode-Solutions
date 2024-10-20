class Solution(object):
    def searchMatrix(self, matrix, target):
        i,j=0,0
        for i in range(len(matrix)):#traversing the row
            for j in range(len(matrix[i])):#changing the row after the input i is reached
                if matrix[i][j]==target:
                    return True
        return False
    