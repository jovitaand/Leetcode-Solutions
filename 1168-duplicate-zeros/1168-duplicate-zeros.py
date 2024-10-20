class Solution: 
    def duplicateZeros(self, arr):
        i=0
        while i < len(arr):
            if arr[i]== 0:
                arr.insert(i+1,0)
                i=i+2
                arr.pop()
                  #popping the last two elements to keep the size of the array same
            else:
                i=i+1
        return arr
        