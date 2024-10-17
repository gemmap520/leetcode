class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        first = True
        sign = 1
        for i in s:
            if i.isdigit():
                result = result * 10 + int(i)
                first = False
            elif i == '+':
                if first:
                    sign = 1
                    first = False
                else:
                    break
            elif i == '-':
                if first:
                    sign = -1
                    first = False
                else:
                    break
            elif i == ' ':
                if first:
                    continue
                else:
                    break
            else:
                break
        result *= sign

        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        return result
