# min cost climbing stairs
# https://neetcode.io/problems/min-cost-climbing-stairs/question
# code by aveia@github

class Solution:

    # def minCostClimbingStairs(self, cost: list[int]) -> int:

    #     cost_to_top = len(cost) * [None]
    #     cost_to_top[-1] = cost[-1]
    #     cost_to_top[-2] = cost[-2]

    #     for i in range(2, len(cost)):
    #         idx = len(cost) - i - 1
    #         step_cost = cost[idx]
    #         cost_to_top[idx] = min(
    #             cost_to_top[idx + 1] + step_cost,
    #             cost_to_top[idx + 2] + step_cost,
    #         )

    #     return min(cost_to_top[0], cost_to_top[1])

    # def minCostClimbingStairs(self, cost: list[int]) -> int:

    #     for i in range(2, len(cost)):
    #         idx = len(cost) - i - 1
    #         cost[idx] = min(
    #             cost[idx + 1] + cost[idx],
    #             cost[idx + 2] + cost[idx],
    #         )

    #     return min(cost[0], cost[1])

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
