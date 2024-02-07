from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.mem = [ -1 ] * len(s)
        return self._helper(s, wordDict, 0)

    def _helper(self, s, wordDict, i):
        if i == len(s): 
            return True
        elif self.mem[i] == -1:
            for word in wordDict:
                if len(word) + i <= len(s) and s[i:len(word)] == word:
                    self.mem[i] = int(self._helper(s, wordDict, i + len(word)))
                    if bool(self.mem[i]):
                        return True
            self.mem[i] = 0
        
        return bool(self.mem[i])
    
if __name__ == "__main__":
    # test = Solution()

    # test.wordBreak()
    print([-1]*10)