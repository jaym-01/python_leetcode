from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.mem = {len(nums) - 1: nums[-1]}
        return self.helper(0, nums)
    
    def helper(self, i: int, nums: List[int]) -> int:
        if i >= len(nums):
            return 0
        elif i not in self.mem:
            self.mem[i] = max(nums[i] + self.helper(i + 2, nums), nums[i+1] + self.helper(i + 3, nums))

        return self.mem[i]
    
if __name__ == "__main__":
    test = Solution()

    print(test.rob([2,7,9,3]))