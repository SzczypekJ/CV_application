from typing import List


class Solution:
    def specialArray(self, nums: List[int]):
        nums.sort(reverse=True)
        for i in range(len(nums)):
            print("nums[i]:", nums[i])
            print("i:", i)
            if nums[i] >= i + 1 and (i == len(nums) - 1 or nums[i + 1] < i + 1):
                return i + 1
        return -1


sol = Solution()
# print(sol.specialArray([0, 4, 3, 0, 4]))
# print(sol.specialArray([3, 5]))
# print(sol.specialArray([0, 0]))
print(sol.specialArray([3, 6, 7, 7, 0]))
