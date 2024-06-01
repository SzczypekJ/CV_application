"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome."""


from collections import Counter


class Solution:
    def isPalindrome(self, s: str):
        if s is None:
            return True

        s = s.lower()
        clean_string = [
            string for string in s if string.isalnum() or string.isspace()]
        clean_string = "".join(clean_string)

        # Usunięcie spacji
        clean_string = clean_string.replace(" ", "")

        return clean_string == clean_string[::-1]


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
