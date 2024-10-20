class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        greatest_num = max(candies)                                  
        return [(candy + extraCandies >= greatest_num) for candy in candies]