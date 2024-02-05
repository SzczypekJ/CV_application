"""You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

 

Example 1:

Input: prices = [1,2,2], money = 3
Output: 0
Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.
Example 2:

Input: prices = [3,2,3], money = 3
Output: 3
Explanation: You cannot buy 2 chocolates without going in debt, so we return 3."""


class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        # My solution:
        sorted_prices = sorted(prices)

        if sorted_prices[0] + sorted_prices[1] == money:
            return 0
        elif sorted_prices[0] + sorted_prices[1] > money:
            return money
        else:
            return money - sorted_prices[0] - sorted_prices[1]

        # Second solution:
        # Assume the Minimum Cost to be Infinity
        # min_cost = float('inf')

        # # Number of Chocolates
        # n = len(prices)

        # # Check Every Pair of Chocolates
        # for first_choco in range(n):
        #     for second_choco in range(first_choco + 1, n):
        #         # Sum of Prices of the Two Chocolates
        #         cost = prices[first_choco] + prices[second_choco]

        #         # If the Sum of Prices is Less than the Minimum Cost
        #         if cost < min_cost:
        #             # Update the Minimum Cost
        #             min_cost = cost

        # # We can buy chocolates only if we have enough money
        # if min_cost <= money:
        #     # Return the Amount of Money Left
        #     return money - min_cost
        # else:
        #     # We cannot buy chocolates. Return the initial amount of money
        #     return money


sol = Solution()
print(sol.buyChoco([1, 2, 2], 3))
print(sol.buyChoco([3, 2, 3], 3))
