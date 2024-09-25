class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i, point in enumerate(points):
            d = -1 * math.sqrt(point[0] ** 2 + point[1] ** 2)
            if i < k:
                heappush(heap, (d, point))
            else:
                top = heappop(heap)
                if d > top[0]:
                    heappush(heap, (d, point))
                else:
                    heappush(heap, top)

        return [val[1] for val in heap]
