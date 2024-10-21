class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        best_costs = [0] * len(cost)
        best_costs[-1] = cost[-1]
        best_costs[-2] = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            best_costs[i] = min(cost[i] + best_costs[i + 1], cost[i] + best_costs[i + 2])
        
        return min(best_costs[0], best_costs[1])
