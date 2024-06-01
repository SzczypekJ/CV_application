"""Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]"""

from typing import List
# sol 1


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output


solution = Solution()
print(solution.subsets([1, 2, 3]))
# sol 2


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         output = [[]]

#         for num in nums:
#             # Utwórz nową listę, aby przechowywać nowe podzbiory, które zostaną dodane
#             new_subsets = []
#             for curr in output:
#                 # Skopiuj bieżący podzbiór i dodaj do niego bieżący element num
#                 new_subset = curr + [num]
#                 new_subsets.append(new_subset)
#             # Dodaj wszystkie nowe podzbiory do output
#             output.extend(new_subsets)

#         return output
