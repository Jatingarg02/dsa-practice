class Solution(object):
    def maxProfit(self, prices):

        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            current_profit = prices[j] - prices[i]
            if prices[i] < prices[j]:
                max_profit = max(current_profit , max_profit)
            else:
                i = j
            j += 1
        return max_profit




        