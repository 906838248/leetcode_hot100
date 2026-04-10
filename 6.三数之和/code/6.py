from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        三数之和 - 排序 + 双指针法
        
        时间复杂度：O(n²)
        空间复杂度：O(1)
        
        算法步骤：
            1. 对数组进行排序
            2. 遍历数组，固定第一个数 nums[i]
            3. 使用双指针 left 和 right 找两数之和
            4. 根据和的大小移动指针
            5. 跳过重复元素避免重复三元组
            6. 剪枝优化提前终止
        
        Args:
            nums: 输入的整数数组
            
        Returns:
            List[List[int]]：所有和为0的不重复三元组
        """
        n = len(nums)
        result = []
        
        # 边界情况：数组长度小于3
        if n < 3:
            return result
        
        # 对数组排序（关键步骤！）
        nums.sort()
        
        # 遍历数组，固定第一个数
        for i in range(n - 2):
            # 跳过重复的 nums[i]，避免重复三元组
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 剪枝：如果最小的三数之和都大于0，无需继续
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            
            # 剪枝：如果最大的三数之和都小于0，跳过这个 nums[i]
            if nums[i] + nums[n - 1] + nums[n - 2] < 0:
                continue
            
            # 双指针查找
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # 找到一个满足条件的三元组
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的 left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # 跳过重复的 right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 移动指针继续查找
                    left += 1
                    right -= 1
                
                elif total < 0:
                    # 总和小于0，左指针右移增大和
                    left += 1
                
                else:
                    # 总和大于0，右指针左移减小和
                    right -= 1
        
        return result