# note this passes all tests in leetcode but there is a problem:
# it fails the test case [1, 100, 1]
# this can be resurrected by uncommenting the lines below
# but they increase the time complexity significantly
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        max_s = -1

        while start < end:
            h_start = height[start]
            h_end = height[end]

            max_s = max(max_s, (end - start) * min(h_start, h_end))

            if h_start < h_end:
                start += 1
            elif h_start > h_end:
                end -= 1
            else:
                # max_s = max(max_s, self.maxArea(height[start+1:end+1]))
                # max_s = max(max_s, self.maxArea(height[start:end]))
                # break
                start += 1
                end -= 1

        return max_s
            
