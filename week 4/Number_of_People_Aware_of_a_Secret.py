class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1 
        total = 0

        for day in range(1, n + 1):
            sharers = dp[day]
            if sharers == 0:
                continue
            for next_day in range(day + delay, min(n + 1, day + forget)):
                dp[next_day] = (dp[next_day] + sharers) % MOD

        for day in range(n - forget + 1, n + 1):
            total = (total + dp[day]) % MOD

        return total        