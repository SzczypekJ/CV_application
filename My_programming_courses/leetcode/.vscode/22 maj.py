"""Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]"""


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palidorme(s):
            return s == s[::-1]

        def backtracing_fun(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palidorme(s[start:end]):
                    backtracing_fun(end, path + [s[start:end]])

        result = []
        backtracing_fun(0, [])
        return result


s = "aab"
sol = Solution()
print(sol.partition(s))


# Działa jeśli mamy tylko sprawdzić czy dany subset jest palidorme ale nie rozwiązuje zadania :(
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         def create_subsets(s):
#             output = [[]]

#             for letter in s:
#                 output += [curr + [letter] for curr in output]

#             output = [ele for ele in output if ele != []]
#             return output

#         subsets = create_subsets(s)
#         result = []
#         for subset in subsets:
#             sep = ''
#             subset = sep.join(subset)
#             if subset == subset[::-1]:
#                 result.append(subset)

#         return result
