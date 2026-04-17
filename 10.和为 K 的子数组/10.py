from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        和为 K 的子数组 - 前缀和+哈希表法

        时间复杂度：O(n)
        空间复杂度：O(n)

        核心思想：
            - 计算前缀和：prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
            - 子数组 [left, right] 的和 = prefix[right+1] - prefix[left]
            - 我们需要找 prefix[right+1] - prefix[left] == k
            - 即 prefix[left] == prefix[right+1] - k
            - 使用哈希表记录每个前缀和出现的次数
        """
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            result += prefix_count[prefix - k]
            prefix_count[prefix] += 1

        return result

a = Solution()
s = [1,2,3]
k = 3
print(a.subarraySum(s, k))

s2 = [1,1,1]
k2 = 2
print(a.subarraySum(s2, k2))