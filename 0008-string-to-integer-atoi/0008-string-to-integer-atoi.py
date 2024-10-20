class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -2**31
        MAX = 2**31-1
        
        sign = 1
        n = 0
        empty = True
        
        for c in s:
            if empty:
                if c == " ":
                    continue
                elif c == "+":
                    sign = 1
                elif c == "-":
                    sign = -1
                elif c.isdigit():
                    n = int(c)
                else:
                    return 0
                empty = False
            else:
                if c.isdigit():
                    n = n*10 + int(c)
                    if sign*n > MAX: return MAX
                    elif sign*n < MIN: return MIN
                
                else:
                    break
        
        return sign*n
        
     
                
                
                
           