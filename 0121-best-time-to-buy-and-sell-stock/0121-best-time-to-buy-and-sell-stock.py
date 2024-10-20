class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        start = 0
        for i in range(1,len(prices)):
            if prices[i]<prices[start]:
                start = i
            else:
                profit = max(profit,prices[i]-prices[start])
        return profit
    #using 2 pointers to identify the best time to buy and sell