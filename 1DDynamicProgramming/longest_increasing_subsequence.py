class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            tmp = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    tmp = max(tmp, 1 + mem[j])
            
            mem[i] = tmp
        
        return max(mem)
