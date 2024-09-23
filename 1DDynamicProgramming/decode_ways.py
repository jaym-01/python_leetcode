class Solution:
    mem = {
        "": 1,
    }

    def numDecodings(self, s: str) -> int:
        if s in self.mem:
            return self.mem[s]
        if s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1
        
        else:
            c = s[0]

            it1 = self.numDecodings(s[1:])
            it2 = 0

            if c == "1" or (c == "2" and ord(s[1]) < ord("7")):
                it2 = self.numDecodings(s[2:])
            
            self.mem[s] = it1 + it2
            return self.mem[s]

