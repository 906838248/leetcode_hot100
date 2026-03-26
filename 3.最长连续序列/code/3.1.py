# 排序法
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        count = 1
        max_count = 1
        if(not nums): return 0
        for i,num in enumerate(nums_sort):
            if(i != len(nums_sort)-1):
                if(nums_sort[i+1]==num+1):
                    count += 1
                elif(nums_sort[i+1]==num):
                    continue
                else:
                    count = 1
            if(max_count<count):
                max_count=count
        return max_count
