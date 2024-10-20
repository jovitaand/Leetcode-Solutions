class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        i=0
        j=0
        count=0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i]==stones[j]:
                    count+=1
        return count