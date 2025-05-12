class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != cur:
                nums[k] = nums[i]
                cur = nums[i]
                k+=1
        return k

