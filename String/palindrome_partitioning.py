from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.mem = {}
        self.mem[len(s) - 1] = [[s[-1]]]
        self.mem[len(s)] = [[]]
        return self.helper(s, 0)


    def helper(self, s, i):
        if i in self.mem:
            return self.mem[i]
        else:
            out = []
            start = i
            i += 1

            while i <= len(s):
                if self.valPalidrome(s, start, i - 1):    
                    for palindrome in self.helper(s, i): 
                        out.append([s[start:i]] + palindrome)
                i += 1

            self.mem[start] = out
            return out
        
    def valPalidrome(self, s, l, r):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    

if __name__ == "__main__":
    test = Solution()
    print(test.partition("aa"))