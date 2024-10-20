class Solution(object):
    def isPalindrome(self, s):
        s = [i for i in s.lower() if i.isalnum()] #stripping the alphabets and reducing it to lower case
        return s==s[::-1] #checking palindrome conditions
    #we put two :: as it acts as a slice operation: first element is the start, last element and last element is the offset
      