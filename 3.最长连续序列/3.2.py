# 哈希
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        max_count = 1
        count = 1

        for num in nums_set:
            if num-1 not in nums_set:
                now_num = num 
                while now_num+1 in nums_set:
                    count +=1
                    now_num += 1
            if max_count<count:
                max_count = count
            count = 1
        return max_count        
                    

        



