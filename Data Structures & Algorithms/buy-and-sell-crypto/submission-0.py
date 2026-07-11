class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # init vars
        buyDay = 0
        buyPrice: int = prices[0]
        maxProfit = 0

        # walk through the list keeping track of:
        # lowest price and best profit opportunity buying/selling from then
        for day, price in enumerate(prices):
            # profit from buying on cheapest day seen and selling today
            profit = price - buyPrice

            # negative profit means a new buying opportunity
            if profit < 0:
                buyPrice = price
                buyDay = day
                
            # check if the profit was a new max
            elif profit > maxProfit:
                maxProfit = profit
        return maxProfit
        