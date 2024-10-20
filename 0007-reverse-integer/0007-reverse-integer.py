class Solution:
    def reverse(self, x):
        MAX = 2**31-1
        MIN = -2**31
        flag = False
        
        'convert int to str'
        char = str(x)
        
        'if it is negative rise a flag'
        if char[0]=='-':
            char = char[1:] #start after the negative sign
            flag = True
            
        'reverse a string'
        rev=char[::-1]
        
        'putting back the minus sign'
        if flag == True:
            rev = '-'+ rev
        
        'convert back string into int'
        rev= int(rev)
        
        'checking out of bounds conditions'
        if rev > MAX or rev < MIN: rev=0
        return rev
        
        
 
 

         
         
      