from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        最大子数组和 - Kadane算法（动态规划/贪心）

        时间复杂度：O(n)
        空间复杂度：O(1)

        算法思想：
            1. 如果前面的子数组和是负数，丢弃它（对当前和没有正向贡献）
            2. 从当前元素重新开始，或加上前面积累的和
            3. 维护全局最大和
        """
        max_current = nums[0]
        max_global = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_global, max_current)

        return max_global


def test():
    sol = Solution()

    # 示例1
    result1 = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(f"示例1: {result1}")
    print(f"期望: 6")
    print(f"通过: {result1 == 6}\n")

    # 示例2
    result2 = sol.maxSubArray([1])
    print(f"示例2: {result2}")
    print(f"期望: 1")
    print(f"通过: {result2 == 1}\n")

    # 示例3
    result3 = sol.maxSubArray([5, 4, -1, 7, 8])
    print(f"示例3: {result3}")
    print(f"期望: 23")
    print(f"通过: {result3 == 23}\n")

    # 额外测试：全负数数组
    result4 = sol.maxSubArray([-1, -2, -3])
    print(f"测试4（全负数）: {result4}")
    print(f"期望: -1")
    print(f"通过: {result4 == -1}\n")

    # 额外测试：包含0
    result5 = sol.maxSubArray([-2, 0, -1])
    print(f"测试5（含0）: {result5}")
    print(f"期望: 0")
    print(f"通过: {result5 == 0}\n")


if __name__ == "__main__":
    test()
