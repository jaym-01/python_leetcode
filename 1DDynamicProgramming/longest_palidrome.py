class Solution:
    def longestPalindrome(self, s: str) -> str:
        mem = [["" for i in range(len(s))] for i in range(len(s))]

        def find_longest_palindrome(start, end):
            s_val = start
            e_val = end
            if start < 0 or end >= len(s):
                return ""
            elif mem[s_val][e_val] == "":
                while start > -1 and end < len(s) and s[start] == s[end]:
                    start -= 1
                    end += 1
                
                start += 1
                end -= 1

                mem[s_val][e_val] = s[start:end + 1] if s[start] == s[end] else s[start]
            return mem[s_val][e_val]

        def solution(i):
            s1 = find_longest_palindrome(i - 1, i + 1)
            s2 = find_longest_palindrome(i - 1, i)
            s3 = find_longest_palindrome(i, i + 1)

            if len(s2) > len(s1):
                s1 = s2
            if len(s3) > len(s1):
                s1 = s3

            return s1
        
        cur_max = 1
        out = s[0]
        for i in range(len(s)):
            tmp = solution(i)
            if len(tmp) > cur_max:
                out = tmp
                cur_max = len(tmp)
        
        return out
