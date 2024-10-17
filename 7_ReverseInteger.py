class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        digit_list = []

        while x > 0:
            r = x % 10
            digit_list.append(r)
            x = x // 10
        result = 0
        for i in digit_list:
            result = result * 10 + i
        result *= sign
        if result > 2**31 - 1 or result < -2**31:
            return 0
        return result
