"""Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1"""

from collections import Counter


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        number_of_elements = Counter(arr)

        for number, amount in number_of_elements.items():
            if amount > 0.25 * len(arr):
                return number


test = Solution()

print(test.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
