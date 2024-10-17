class Solution:
    def intToRoman(self, num: int) -> str:
        lst = [['M', 1000], ['CM', 900], ['D', 500], ['CD',  400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
        result = ""
        for i in lst:
            q = num // i[1]
            r = num % i[1]
            it = 0
            if i[1] % 9 == 0 or i[1] == 4 or i[1] == 40 or i[1] == 400:
                if q == 1:
                    it = q
                    num = r
            else:
                it = q
                num = r
            for j in range(it):
                result += i[0]
        return result

        
