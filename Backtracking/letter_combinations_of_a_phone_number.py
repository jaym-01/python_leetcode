from typing import List 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        cs = self.getdigits(digits[0])

        next = self.letterCombinations(digits[1:])

        if len(next) == 0:
            return cs
	
        out = []

        for i in range(len(cs)):
            tmp = next.copy()
            for j in range(len(tmp)):
                tmp[j] = cs[i] + tmp[j]
            out += tmp
	
        return out

    def getdigits(n):
        start = (n-2)*3+97
        out = []

        for i in range(3):
            out.append(chr(start+i))

        if n == 9:
            out.append(chr(start+3))
        return out