from typing import List
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        最小覆盖子串 - 滑动窗口法

        时间复杂度：O(m + n)
        空间复杂度：O(m + n)

        算法步骤：
            1. 用哈希表记录 t 中每个字符需要的数量
            2. 用双指针维护滑动窗口
            3. 扩大右指针，添加字符到窗口
            4. 当窗口满足条件时，收缩左指针找最小窗口
            5. 重复直到遍历完整个字符串
        """
        if len(t) > len(s):
            return ""
        
        need_count = defaultdict(int)
        window = defaultdict(int)
        
        for char in t:
            need_count[char] += 1
        
        required = len(need_count)
        formed = 0
        left = 0
        min_length = float('inf')
        min_window = ""
        
        for right, char in enumerate(s):
            window[char] += 1
            
            if char in need_count and window[char] == need_count[char]:
                formed += 1
            
            while formed == required:
                current_length = right - left + 1
                
                if current_length < min_length:
                    min_length = current_length
                    min_window = s[left:right+1]
                
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in need_count and window[left_char] < need_count[left_char]:
                    formed -= 1
                
                left += 1
        
        return min_window

a = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(a.minWindow(s, t))

s2 = "a"
t2 = "a"
print(a.minWindow(s2, t2))

s3 = "a"
t3 = "aa"
print(a.minWindow(s3, t3))