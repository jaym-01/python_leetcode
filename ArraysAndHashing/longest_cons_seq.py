class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        all_vals = set(nums)
        mem = {}

        longest = 1

        for n in nums:
            if n in all_vals:
                all_vals.remove(n)
                cur = n + 1
                count = 1

                while cur in all_vals:
                    all_vals.remove(cur)
                    count += 1
                    cur += 1

                if cur in mem:
                    count += mem[cur]
                mem[n] = count
                
                longest = max(longest, count)

        return longest
