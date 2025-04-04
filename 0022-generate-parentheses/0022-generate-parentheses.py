class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack( S+'(',left+1,right)
            if right < left:
                backtrack( S+')', left, right+1)
        backtrack()
        return ans