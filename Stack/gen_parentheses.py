class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solution(openb: int, closedb: int) -> List[str]:
            if openb == n and closedb == n:
                return [""]
            elif openb > closedb:
                out = []
                # only open a new bracket if not past the limit
                if openb < n:
                    out += ["(" + b for b in solution(openb + 1, closedb)]
                
                # you can always close when there are more open brackets
                out += [")" + b for b in solution(openb, closedb + 1)]

                return out

            else:
                # case where they are equal -> impossible for openb < closedb
                return ["(" + b for b in solution(openb + 1, closedb)]
        
        return solution(0, 0)
