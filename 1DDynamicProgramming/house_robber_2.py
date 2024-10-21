class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        w_e = nums[-1]
        wo_e = nums[-2]
        prev = (nums[-3] + nums[-1], max(nums[-3], nums[-2]))

        for i in range(len(nums) - 4, 0, -1):
            tmp = (nums[i] + w_e, nums[i] + wo_e)
            w_e = max(w_e, prev[0])
            wo_e = max(wo_e, prev[1])
            prev = tmp
        
        return max(nums[0] + wo_e, w_e, prev[0], prev[1])
