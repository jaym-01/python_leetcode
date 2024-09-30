class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mem = [[-1 for j in range(len(matrix[i]))] for i in range(len(matrix))]

        def find_longest_path(x, y, prev):
            if y < 0 or x < 0 or y >= len(matrix) or x >= len(matrix[y]) or prev >= matrix[y][x]:
                return 0
            elif mem[y][x] != -1:
                return mem[y][x]
            else:
                cur_val = matrix[y][x]

                mem[y][x] = max([
                    find_longest_path(x + 1, y, cur_val),
                    find_longest_path(x, y + 1, cur_val),
                    find_longest_path(x - 1, y, cur_val),
                    find_longest_path(x, y - 1, cur_val)
                ]) + 1

                return mem[y][x]

        max_len = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                max_len = max(max_len, find_longest_path(x, y, matrix[y][x] - 1))
        
        return max_len
