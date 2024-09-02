class Solution:
    def traverse(self, s: str, l: int, r: int) -> int:
        total = 0

        while l > -1 and r < len(s) and s[l] == s[r]:
            total += 1
            l -= 1
            r += 1

        return total

    def countSubstrings(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            total += 1

            total += self.traverse(s, i - 1, i + 1)
            total += self.traverse(s, i, i + 1)

        return total
