class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]
        elif len(nums) == 1: return [[], nums]
        else:
            print(nums[1:])
            exclude = self.subsets(nums[1:])
            out = [*exclude]
            for arr in exclude:
                out.append([*arr, nums[0]])
            return out
