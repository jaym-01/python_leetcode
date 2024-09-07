class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[-1] * n for _ in range(m)]
        mem[-1][-1] = 1

        return self.helper(0, 0, mem)

    def helper(self, i: int, j: int, mem: list[list[int]]):
        if j < len(mem) and i < len(mem[j]):
            if mem[j][i] != -1:
                return mem[j][i]
            else:
                val = self.helper(i + 1, j, mem) + self.helper(i, j + 1, mem)
                mem[j][i] = val
                return val
        else:
            return 0
