class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = deepcopy(nums[:k])
        heapify(heap)

        for i in range(k, len(nums)):
            cur_smallest = heappop(heap)

            if cur_smallest < nums[i]:
                heappush(heap, nums[i])
            else:
                heappush(heap, cur_smallest)

        return heappop(heap)
