class Solution(object):
    def intToRoman(self, num):
        M = ["","M","MM","MMM"]
        C = ["", "C", "CC", "CCC","CD","D", "DC", "DCC", "DCCC" ,"CM"]
        X = ["", "X", "XX","XXX","XL", "L","LX","LXX","LXXX","XC"]
        I = ["", "I","II","III","IV","V","VI","VII","VIII","IX"]
        
        return M [num//1000] + C [(num//100)%10] + X [(num//10)%10] + I [num%10]
    
    
  
         
         
    
    