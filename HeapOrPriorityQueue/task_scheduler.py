class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}
        for task in tasks:
            if task in task_count:
                task_count[task] += 1
            else:
                task_count[task] = 1

        queue = []
        heap = []

        for count in task_count.values():
            heappush(heap, -1 * count)

        it = 0
        while len(heap) > 0 or len(queue) > 0:
            if len(queue) > 0:
                while len(queue) > 0 and queue[0][1] <= it:
                    heappush(heap, queue[0][0])
                    queue.pop(0)
            
            if len(heap) > 0:
                top = heappop(heap)
                top += 1
                if top < 0:
                    queue.append((top, it + n + 1))

            
            it += 1

        return it


