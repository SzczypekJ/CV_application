"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution 1
        stairs = [0] * n
        if n >= 1:
            stairs[0] = 1
        if n >= 2:
            stairs[1] = 2

        for i in range(2, n):
            stairs[i] = stairs[i-1] + stairs[i-2]

        return stairs[n-1]

        # solution 2
        # ways = 1

        # for i in range(1, (n // 2) + 1):
        #     product = 1

        #     for j in range(i, 2 * i):
        #         product *= (n - j) / (j - i + 1)

        #     ways += product

        # return int(ways)