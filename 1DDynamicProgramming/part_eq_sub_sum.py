class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n_sum = sum(nums)

        if n_sum % 2 != 0:
            return False
        else:
            target = n_sum // 2

            sums = set([nums[-1], 0])
            print(sums)

            for i in range(len(nums) - 2, -1, -1):
                if target in sums:
                    return True
                else:
                    tmp = list(sums)

                    for e in tmp:
                        sums.add(e + nums[i])

                    sums.add(nums[i])

            return target in sums
