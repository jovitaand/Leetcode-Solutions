class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum,accounts)) # map() function iterates the sum of every account and max() gives result