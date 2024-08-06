class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_days = days[-1]
        day_set = set(days)
        dp = [0] * (max_days+1)
        for i in range(1,len(dp)):
            if i in day_set:
                dp[i] = min(
                    costs[0]+ dp[i-1],
                    costs[1] + dp[max((i-7),0)],
                    costs[2] + dp[max((i-30),0)]
                )
            else:
                dp[i] = dp[i-1]
        return dp[-1]

"""
Time and space : O(1)
"""
        
