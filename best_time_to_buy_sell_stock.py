class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # the objective here can be encapsulated in famous saying: "buy low sell high"
        prices_global_min = min(prices)
        prices_global_max = max(prices)
        if prices.index(prices_global_max) > prices.index(prices_global_min):
            current_transaction_profit = prices_global_max-prices_global_min
            return current_transaction_profit
        else:
            prices_local_min = prices[0]
            current_transaction_profit = 0
            for i in range(len(prices)):
                if (prices[i] < prices_local_min):
                    prices_local_min = prices[i]
                elif (prices[i] - prices_local_min > current_transaction_profit):
                    current_transaction_profit = prices[i] - prices_local_min
            return current_transaction_profit