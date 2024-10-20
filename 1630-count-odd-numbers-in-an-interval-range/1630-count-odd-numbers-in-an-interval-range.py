class Solution(object):
    def countOdds(self, low, high):
        if low % 2 == 1:
            low -=1
        if high % 2 ==1:
            high +=1
        return int((high - low) / 2)