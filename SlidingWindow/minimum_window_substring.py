import sys

class Solution:
    def convert_to_dict(self, t: str) -> dict:
        return {i: t.count(i) for i in set(list(t))}

    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        t_dict = self.convert_to_dict(t)
        print(t_dict)

        start = 0
        end = 0
        min_start = 0
        min_end = sys.maxsize
        # print(min_end)
        char_count = len(t)

        while end < len(s):
            while char_count > 0 and end < len(s):
                if s[end] in t_dict:
                    print("here")
                    t_dict[s[end]] -= 1
                    if t_dict[s[end]] >= 0:
                        char_count -= 1
                        print("here: ", end)
                end += 1
            
            while start < end:
                if s[start] in t_dict and char_count > 0:
                    break
                elif s[start] in t_dict:
                    t_dict[s[start]] += 1
                    print("here")
                    if min_end - min_start > end - start:
                        min_start = start
                        min_end = end
                    if t_dict[s[start]] > 0:
                        char_count += 1
                start += 1
                
        return "" if min_end == sys.maxsize else s[min_start:min_end]

if __name__ == "__main__":
    test = Solution()

    print(test.minWindow("ab", "a"))