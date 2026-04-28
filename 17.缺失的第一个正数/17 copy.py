from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums_set = {i for i in range(1,n+2)}
        for num in nums:
            if(num in nums_set):
                nums_set.remove(num)
        return min(nums_set)