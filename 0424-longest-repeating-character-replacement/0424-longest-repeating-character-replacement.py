class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 +  count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
        return ( r - l + 1)