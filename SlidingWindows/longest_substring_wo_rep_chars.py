class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 0:
            start = 0
            chars = set([s[0]])
            max_len = 1

            for i in range(1, len(s)):
                if s[i] in chars:
                    max_len = max(max_len, i - start)
                    while s[i] in chars and start <= i:
                        chars.remove(s[start])
                        start += 1
                chars.add(s[i])


            if start != len(s) - 1:
                max_len = max(max_len, len(s) - start)
            return max_len
        else:
            return 0

