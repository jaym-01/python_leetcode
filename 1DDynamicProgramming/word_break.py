class Solution:
    def wordBreak(self, s1: str, wordDict: List[str]) -> bool:
        mem = set([])
        def solution(s, mem):
            if s == "":
                return True
            elif s not in mem:
                for w in wordDict:
                    if s[:len(w)] == w:
                        if solution(s[len(w):], mem):
                            return True
                    
                mem.add(s)
            return False

        return solution(s1, mem)
