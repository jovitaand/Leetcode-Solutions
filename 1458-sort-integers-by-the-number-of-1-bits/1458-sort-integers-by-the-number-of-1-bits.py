class Solution(object):
    def sortByBits(self, arr):
    
        bin_cnt = [] #bin function is used for converting decimal to binary
        for i in arr:
            bin_cnt.append(bin(i).count('1'))
        ans = sorted(list(zip(bin_cnt, arr)))
        return [i[1] for i in ans]
    #The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
                