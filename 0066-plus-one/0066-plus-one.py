class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(e) for e in digits)) #uses the join function to join all the          integers
        num2= num +1 # increments
        res = [int(i) for i in str(num2)] #converts integers back into string
        return res # result as a list