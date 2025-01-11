class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [[-1] * n for i in range(n)]

        # form adjacency matrix
        # create a fully connected graph with all points found
        for i in range(n - 1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                graph[i][j] = d
                graph[j][i] = d

        visited = set([])
        frontier = [(0,0)]
        cost = 0

        while len(visited) != n:
            tmpCost, node = heappop(frontier)

            # remove values that have already been visited
            while node in visited:
                tmpCost, node = heappop(frontier)
            
            # visiting the current node which is the shortest distance to get to
            cost += tmpCost
            visited.add(node)

            # add all of the neighbours to the frontier
            # as long as they have not been visited
            neighbours = graph[node]
            for node, d in enumerate(neighbours):
                if node in visited:
                    continue
                heappush(frontier, (d, node))

        return cost


