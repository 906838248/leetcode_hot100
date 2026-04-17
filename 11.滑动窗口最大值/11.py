from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        滑动窗口最大值 - 单调递减队列法

        时间复杂度：O(n)
        空间复杂度：O(k)

        算法步骤：
            1. 使用双端队列存储元素的索引
            2. 队列中的元素按值单调递减排列
            3. 队首始终是当前窗口的最大值
            4. 每次移动窗口时：
               - 添加新元素，移除比它小的元素
               - 移除超出窗口范围的元素（索引 < i-k+1）
        """
        if not nums or k == 0:
            return []
        
        result = []
        deque_index = deque()
        
        for i in range(len(nums)):
            # 1. 添加新元素：移除队列中所有比当前元素小的元素
            while deque_index and nums[deque_index[-1]] < nums[i]:
                deque_index.pop()
            
            # 2. 添加当前元素的索引
            deque_index.append(i)
            
            # 3. 移除超出窗口范围的元素
            if deque_index[0] <= i - k:
                deque_index.popleft()
            
            # 4. 当窗口形成后，记录最大值
            if i >= k - 1:
                result.append(nums[deque_index[0]])
        
        return result

a = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = a.maxSlidingWindow(nums, k)
print(f"结果: {result}")
print(f"期望: [3, 3, 5, 5, 6, 7]")
print(f"通过: {result == [3, 3, 5, 5, 6, 7]}")