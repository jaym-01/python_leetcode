class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        mem = [-2] * (amount + 1)

        def solution(n, mem):
            if n < 0:
                return -1
            elif n == 0:
                return 0
            elif mem[n] == -2:
                min_coins = -1
                for coin in coins:
                    tmp = solution(n - coin, mem)
                    if tmp != -1 and (min_coins == -1 or tmp + 1 < min_coins):
                        min_coins = tmp + 1
                
                mem[n] = min_coins
            return mem[n]

        return solution(amount, mem)
