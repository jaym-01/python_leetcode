class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []

        for c in s:
            if c in close:
                stack.append(c)
            elif len(stack) > 0:
                top = stack.pop(-1)
                if close[top] != c:
                    return False
            else:
                return False

        return len(stack) == 0

