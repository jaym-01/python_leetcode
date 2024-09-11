class Solution:
    def twoSum(self, nums: list[int], target: int, start: int):
        out = []

        first = start
        last = len(nums) - 1

        while first < last:
            s = nums[first] + nums[last]

            if s == target:
                out.append((nums[first], nums[last]))
                first += 1
                last -= 1

            elif s > target:
                last -= 1
            else:
                first += 1

        return out

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = set()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            tmp = self.twoSum(nums, nums[i] * -1, i + 1)
            for val in tmp:
                triplets.add((nums[i], val[0], val[1]))
        
        out = [[trip[0], trip[1], trip[2]] for trip in triplets]

        return out

        
