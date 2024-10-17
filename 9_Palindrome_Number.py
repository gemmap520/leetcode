class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        lst = []
        while x > 0:
            lst.append(x % 10)
            x = x // 10
        length = len(lst) - 1
        for i in range(len(lst) - 1):
            if lst[i] != lst[length - i]:
                return False
        return True

