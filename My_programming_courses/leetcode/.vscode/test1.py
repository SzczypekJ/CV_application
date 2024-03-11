from collections import Counter


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter_nums = Counter(nums)
        nums.clear()
        for key, values in counter_nums.items():
            nums.append(key)
        nums.sort()
        return len(nums)


sol = Solution()
# print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expectedNums = [0, 1, 2, 3, 4]

k = sol.removeDuplicates(nums)

assert k == len(expectedNums)
assert nums[:k] == expectedNums