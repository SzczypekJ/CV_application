"""Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space."""

from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for key, value in count.items():
            if value == 1:
                res.append(key)

        return res


nums = [1, 2, 1, 3, 2, 5]
sol = Solution()
print(sol.singleNumber(nums))
