class Solution(object):
    def repeatedCharacter(self, s):
        res = set()
        for c in s:
            if c in res:
                return c
            res.add(c)
        return res
   