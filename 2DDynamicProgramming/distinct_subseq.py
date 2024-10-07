class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mem = [[-1 if len(s) - i >= len(t) - j else 0 for j in range(len(t))] for i in range(len(s) + 1)]

        def solution(i: int, j: int) -> int:
            if s[i:] == t[j:] or len(t) == j:
                return 1
            elif mem[i][j] > -1:
                return mem[i][j]
            else:
                count = 0
                for k in range(i, len(s)):
                    if s[k] == t[j]:
                        count += solution(k + 1, j + 1)
                mem[i][j] = count
                return mem[i][j]
        
        return solution(0, 0)
