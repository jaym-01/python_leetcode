class Solution:
    def climbStairs(self, n: int) -> int:
        self.mem = {}
        return self.helper(0, n)

    def helper(self, sum: int, n: int) -> int:
        if sum == n:
            self.mem[sum] = 1
        elif sum > n:
            self.mem[sum] = 0
        elif sum not in self.mem:
            self.mem[sum] = self.helper(sum + 1, n) + self.helper(sum + 2, n)
        return self.mem[sum]
        
if __name__ == "__main__":
    test = Solution()
    print(test.climbStairs(4))