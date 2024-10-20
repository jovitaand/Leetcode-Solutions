class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        MAX=0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack)== 0:
                    stack.append(i)
                else: 
                    MAX = max(MAX, i-stack[-1])         
        return MAX
        
        