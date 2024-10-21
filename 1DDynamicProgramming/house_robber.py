class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        cur_max = nums[-1]
        prev = nums[-2]
        for i in range(len(nums) - 3, -1, -1):
            tmp = prev
            prev = nums[i] + cur_max
            cur_max = max(cur_max, tmp)

        return max(prev, cur_max)
