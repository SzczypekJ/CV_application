"""You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer."""


class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_good_integer = ""

        for i in range(len(num) - 2):
            if num[i + 1] == num[i] and num[i + 2] == num[i + 1]:
                current_good_integer = num[i:i + 3]
                max_good_integer = max(max_good_integer, current_good_integer)

        return max_good_integer


num = "6777133339"
sol = Solution()
print("solution is:", sol.largestGoodInteger(num))
