import re
class Solution(object):
    def isMatch(self, s, p):
        return re.search("^" + p + "$" ,s)

#Using "^" is for starting character
#Using "$" is for ending character