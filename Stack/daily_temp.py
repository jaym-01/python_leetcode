class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]
        stack = [(temperatures[-1], len(temperatures) - 1)]

        for i in range(len(temperatures) - 2, -1, -1):
            temp = temperatures[i]

            while len(stack) > 0 and stack[-1][0] <= temp:
                stack.pop(-1)

            if len(stack) > 0:
                out.append(stack[-1][1] - i)
            else:
                out.append(0)

            stack.append((temp, i))

        out.reverse()
        return out
