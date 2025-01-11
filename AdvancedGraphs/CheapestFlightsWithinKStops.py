class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}

        for fromi, toi, pricei in flights:
            if fromi not in graph:
                graph[fromi] = []
            graph[fromi].append((toi, pricei))

        heap = [(0, src, -1)]
        visited = {}
        while len(heap) > 0:
            cost, node, stops = heappop(heap)
            if node in visited and stops >= visited[node][1]:
                continue
            elif node == dst:
                return cost

            visited[node] = (cost, stops)
            if node in graph and stops < k:
                for neighbour, price in graph[node]:
                    heappush(heap, (cost+price, neighbour, stops + 1))

        return -1
        
