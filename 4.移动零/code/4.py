
# 前后指针
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        while(left<right):
            if(nums[right]==0):right -= 1
            else:
                left += 1
                break
        while(right<left):
            if(nums[right]==0):
                nums.append(0)
                nums.remove(0)
            right += 1
             
