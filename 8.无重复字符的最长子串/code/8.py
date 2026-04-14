class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        无重复字符的最长子串 - 滑动窗口法
        
        时间复杂度：O(n)
        空间复杂度：O(min(m, n))
        
        算法步骤：
            1. 使用字典记录每个字符最后出现的位置
            2. 右指针遍历字符串
            3. 如果遇到重复字符，移动左指针到重复字符之后
            4. 更新最大长度
        
        Args:
            s: 输入字符串
            
        Returns:
            int：无重复字符的最长子串长度
        """
        if not s:
            return 0
        
        char_index = {}
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length