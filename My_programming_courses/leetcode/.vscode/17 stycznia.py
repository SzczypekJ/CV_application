"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true"""

from collections import Counter


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter1 = Counter(arr)
        set1 = set()

        for values in counter1.values():
            if values in set1:
                return False
            set1.add(values)

        return True


sol = Solution()
print(sol.uniqueOccurrences([1, 2]))
print(sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
