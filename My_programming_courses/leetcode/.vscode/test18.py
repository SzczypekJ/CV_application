"""First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        count_s = Counter(s)

        lst1 = []
        for key, value in count_s.items():
            if value == 1:
                lst1.append(key)
        # print(lst1)

        for index, value in enumerate(s):
            # print('index, value: ', index, value)
            if value in lst1:
                return index

        return -1


sol = Solution()
print(sol.firstUniqChar("leetcode"))
# print(sol.firstUniqChar("loveleetcode"))
# print(sol.firstUniqChar("aabb"))
