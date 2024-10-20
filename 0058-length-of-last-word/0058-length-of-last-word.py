class Solution(object):
    def lengthOfLastWord(self, s):
        space, count = 0,0 
        for i in s:
            if i == ' ':
                space+=1
                continue
            if i != ' ' and space != 0:
                count, space = 0,0
            count+=1
        return count