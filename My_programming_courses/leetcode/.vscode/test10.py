"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""


class Solution:
    def twoSum(self, nums, target):
    # Create a dictionary to store the indices of numbers
        num_indices = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if the complement (target - num) exists in the dictionary
            complement = target - num
            if complement in num_indices:
                # Return the indices of the two numbers
                return [num_indices[complement], i]
            # Otherwise, add the current number and its index to the dictionary
            num_indices[num] = i
        
        # If no such pair exists, return None or raise an exception
        return None


sol = Solution()
print(sol.twoSum([3, 2, 4], 6))
