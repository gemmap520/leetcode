class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            prefix_temp = strs[0][i]
            for j in strs:
                if i >= len(j) or j[i] != prefix_temp:
                    return prefix
            prefix += prefix_temp
        return prefix
