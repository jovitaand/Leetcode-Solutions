class Solution(object):
    def fizzBuzz(self, n):
        l=[]
        for i in range(1,n+1):
            if i%3 ==0 and i%5 == 0:
                l.append("FizzBuzz") # divisible with 3 and 5 return FizzBuzz
            elif i % 3 == 0: # divisble with 3 return Fizz
                l.append("Fizz")
            elif i % 5 == 0: # divisble with 5 return Buzz
                l.append("Buzz") 
            else:
                l.append(str(i)) #otherwise return the number as it is 
        return l
    

 
        