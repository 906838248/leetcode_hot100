from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        接雨水 - 双指针法
        
        时间复杂度：O(n)
        空间复杂度：O(1)
        
        算法步骤：
            1. 初始化左右指针和最大高度
            2. 比较左右指针指向的柱子高度
            3. 处理较矮的一边，计算雨水
            4. 移动指针，继续处理
        
        Args:
            height: 表示柱子高度的数组
            
        Returns:
            int：能接住的雨水总量
        """
        n = len(height)
        
        # 边界情况
        if n == 0:
            return 0
        
        # 初始化指针和变量
        left = 0
        right = n - 1
        left_max = 0
        right_max = 0
        water = 0
        
        # 双指针遍历
        while left < right:
            # 如果左边柱子较矮，处理左边
            if height[left] < height[right]:
                # 更新左边最大高度
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # 可以接雨水
                    water += left_max - height[left]
                left += 1
            else:
                # 如果右边柱子较矮或相等，处理右边
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # 可以接雨水
                    water += right_max - height[right]
                right -= 1
        
        return water