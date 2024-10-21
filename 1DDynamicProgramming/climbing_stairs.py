class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else:
            a = 1
            b = 2

            for i in range(n-2):
                tmp = a + b
                a = b
                b = tmp
            return b

# or
class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1] * n
        mem.append(1)
        def solution(cur, mem):
            if cur > n:
                return 0
            elif mem[cur] == -1:
                mem[cur] = solution(cur + 1, mem) + solution(cur + 2, mem)
            return mem[cur]
        return solution(0, mem)
