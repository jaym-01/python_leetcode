class Solution:
    def findIslandArea(self, grid, x, y):
        if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]) or grid[y][x] == -1 or grid[y][x] == 0:
            return 0
        else:
            grid[y][x] = -1
            count = 1

            count += self.findIslandArea(grid, x + 1, y)
            count += self.findIslandArea(grid, x - 1, y)
            count += self.findIslandArea(grid, x, y + 1)
            count += self.findIslandArea(grid, x, y - 1)

            return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                islandArea = self.findIslandArea(grid, x, y)
                if islandArea > maxArea: maxArea = islandArea

        print(grid)
        return maxArea
