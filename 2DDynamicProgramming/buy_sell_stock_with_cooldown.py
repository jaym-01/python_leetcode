class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # key = (i, buy)
        mem = {}

        def dfs(prices, i, buy, mem):
            if i >= len(prices):
                return 0
            elif (i, buy) not in mem:
                if buy:
                    r = dfs(prices, i + 1, not buy, mem) - prices[i]
                    skip = dfs(prices, i + 1, buy, mem)

                else:
                    r = dfs(prices, i + 2, not buy, mem) + prices[i]
                    skip = dfs(prices, i + 1, buy, mem)

                mem[(i, buy)] = max(r, skip)
            return mem[(i, buy)]
        
        return dfs(prices, 0, True, mem)
