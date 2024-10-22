class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = [0] * len(nums)
        # first val = largest num can be produced
        # second val = smallest num can be produced
        prod[-1] = (nums[-1], nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            prod[i] = (max(nums[i], nums[i] * prod[i + 1][0], nums[i] * prod[i + 1][1]), min(nums[i], nums[i] * prod[i + 1][0], nums[i] * prod[i + 1][1]))
        
        return max([max(vals) for vals in prod])
