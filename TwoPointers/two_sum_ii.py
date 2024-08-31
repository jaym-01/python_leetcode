class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, val in enumerate(numbers):            
            s_index = self.binary_search(numbers[i + 1: ], target-val)
            
            if s_index != -1:
                return [i + 1, s_index + 1 + i + 1]
            
    
    def binary_search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        else:
            mid = len(nums) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binary_search(nums[:mid], target)
            elif mid + 1 < len(nums):
                return mid + 1 + self.binary_search(nums[mid + 1:], target)
            else:
                return -1