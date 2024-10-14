class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            out = []
            for i in range(len(nums)):
                poss = self.permute(nums[:i] + nums[i + 1:])
                out += [[nums[i]] + val for val in poss]
            return out
