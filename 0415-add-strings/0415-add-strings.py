class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(f"{num1} + {num2}")) 
    #eval(): evaluates the string and returns a value
    #https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/