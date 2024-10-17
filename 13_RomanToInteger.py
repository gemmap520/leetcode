class Solution:
    def romanToInt(self, s: str) -> int:
        lst = [['M', 1000], ['CM', 900], ['D', 500], ['CD',  400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
        lst = dict(lst)
        i = 0
        result = 0
        while i < len(s):
            two = s[i:i+2]
            if two in lst:
                result += lst[two]
                i += 2
            else:
                result += lst[s[i]]
                i += 1
        return result
    
