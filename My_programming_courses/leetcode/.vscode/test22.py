class Solution:
    def myAtoi(self, s: str):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)

        num *= sign
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num


sol = Solution()
print(sol.myAtoi("   -423"))
