class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # convert to dictionary
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        heap = []
        vals = list(freq.items())
        for i in range(len(vals)):
            e = vals[i][0]
            f = vals[i][1]

            if i < k:
                heap.append(f)
            else:
                if i == k: heapify(heap)

                top = heappop(heap)

                if top < f:
                    heappush(heap, f)
                else:
                    heappush(heap, top)
        
        out = []
        for e, f in vals:
            if f in heap:
                out.append(e)
        
        return out
