from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.mem = {"":True}

        return self.helper(s, wordDict)
    
    def helper(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True
        else:
            # for word in wordDict:
            #     tmp = s.find(word)
            #     while tmp != -1:
            #         left = s[:tmp]
            #         right = s[tmp + len(word):]

            #         self.helper(left, wordDict)

            #         self.helper(right, wordDict)
                    

            #         if self.mem[left] and self.mem[right]:
            #             self.mem[s] = True
            #             return True

            #         tmp = s.find(word, tmp + 1)
            
            # self.mem[s] = False

            for i in range(0, len(s)):
                tmpS = s[:i+1]

                if tmpS in wordDict:
                    if self.helper(s[i+1:], wordDict) == True:
                        return True
                    else:
                        self.mem[tmpS] = False
                else:
                    self.mem[tmpS] = False
        
        return False

if __name__ == "__main__":
    test = Solution()
    print(test.wordBreak("applepenapple", ["apple","pen"]))