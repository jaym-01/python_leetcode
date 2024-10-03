class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()

        while True:
            t = 0
            for c in str(n):
                t += int(c) ** 2
            if t == 1:
                return True
            elif t in found:
                break
            else:
                found.add(t)
                n = t

        return False
