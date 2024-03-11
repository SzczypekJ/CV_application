"""Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca"."""


class Solution:
    def minimumLength(self, s: str) -> int:
        # if string is empty return 0
        if not s:
            return 0

        length = len(s)

        # Checking the prefix and suffix
        while length > 1 and s[0] == s[-1]:
            prefix = s[0]
            suffix = s[-1]

            # Checking how many values from the front are the same
            i = 0
            print("lenght:", length)
            while i < length and s[i] == prefix:
                i += 1
                print("i:", i)

            # Checking how many values from the back are the same
            j = length - 1
            while j >= 0 and s[j] == suffix:
                j -= 1
                print("j:", j)

            # Actualization of lenght and our string
            length = j - i + 1
            print('length_after:', length)
            s = s[i:j+1]
            print('s:', s)
        # we cant return lower than 0
        return max(length, 0)


sol = Solution()
print(sol.minimumLength("cabaabac"))
