class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init vars
        buyPrice: int = prices[0]
        maxProfit = 0

        # walk through the list keeping track of:
        # lowest price and best profit opportunity buying/selling from then
        for price in prices[1:]:
            # profit from buying on cheapest day seen and selling today
            profit = price - buyPrice

            # negative profit means a new buying opportunity
            if profit < 0:
                buyPrice = price
                continue
                
            # check if the profit was a new max
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit