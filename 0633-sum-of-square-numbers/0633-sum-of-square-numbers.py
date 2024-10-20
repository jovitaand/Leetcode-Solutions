class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0 
        high = int(c**(1/2)) # sqrt = 1/2
        while low <= high:
            ans = (low*low) + (high*high)
            if ans == c:
                return True
            elif ans < c:
                    low +=1
            else:
                    high -=1
        return False
                