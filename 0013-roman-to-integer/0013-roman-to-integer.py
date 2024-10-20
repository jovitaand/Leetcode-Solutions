class Solution(object):
    def romanToInt(self, s):
        roman = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if i+1< len(s) and roman[s[i]] < roman[s[i+1]]: #first checking inbound contdition ,if the a small number proceeds bigger one please then we substract the element 
                    result -= roman[s[i]]
            else:
                    result += roman[s[i]]
        return result
    #https://www.youtube.com/watch?v=3jdxYj3DD98