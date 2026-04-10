class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        修正你代码中的问题：
        1. 添加外层去重
        2. 找到三元组后跳过重复值
        3. 去掉 'if chack not in result'
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # 问题1修复：跳过重复的 nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while right > left:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum == 0:
                    # 问题2修复：直接添加，不再检查
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 问题3修复：跳过重复值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 移动指针
                    left += 1
                    right -= 1
                
                elif three_sum > 0:
                    right -= 1
                
                else:
                    left += 1
        
        return result