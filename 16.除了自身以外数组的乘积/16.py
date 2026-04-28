from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        除自身以外数组的乘积 - 前缀后缀法

        时间复杂度：O(n)
        空间复杂度：O(1) - 不计入输出数组

        算法思想：
          1. 第一步：从左到右，计算每个位置的左侧累积乘积
          2. 第二步：从右到左，乘以右侧累积乘积
        """
        n = len(nums)
        if n == 0:
            return []

        answer = [0] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


def test():
    sol = Solution()

    print("=" * 60)
    print("除自身以外数组的乘积测试")
    print("=" * 60)

    # 示例1
    nums1 = [1, 2, 3, 4]
    print(f"\n示例1:")
    print(f"输入: nums = {nums1}")
    result1 = sol.productExceptSelf(nums1)
    print(f"输出: {result1}")
    print(f"期望: [24, 12, 8, 6]")
    print(f"通过: {result1 == [24, 12, 8, 6]}")

    # 示例2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"\n示例2:")
    print(f"输入: nums = {nums2}")
    result2 = sol.productExceptSelf(nums2)
    print(f"输出: {result2}")
    print(f"期望: [0, 0, 9, 0, 0]")
    print(f"通过: {result2 == [0, 0, 9, 0, 0]}")

    # 测试3：包含负数
    nums3 = [-1, -2, -3, -4]
    print(f"\n测试3（全是负数）:")
    print(f"输入: nums = {nums3}")
    result3 = sol.productExceptSelf(nums3)
    print(f"输出: {result3}")
    print(f"期望: [-24, -12, -8, -6]")
    print(f"通过: {result3 == [-24, -12, -8, -6]}")

    # 测试4：包含零
    nums4 = [0, 2, 3, 4]
    print(f"\n测试4（包含零）:")
    print(f"输入: nums = {nums4}")
    result4 = sol.productExceptSelf(nums4)
    print(f"输出: {result4}")
    print(f"期望: [24, 0, 0, 0]")
    print(f"通过: {result4 == [24, 0, 0, 0]}")

    # 测试5：多个零
    nums5 = [0, 0, 2, 3]
    print(f"\n测试5（多个零）:")
    print(f"输入: nums = {nums5}")
    result5 = sol.productExceptSelf(nums5)
    print(f"输出: {result5}")
    print(f"期望: [0, 0, 0, 0]")
    print(f"通过: {result5 == [0, 0, 0, 0]}")

    # 测试6：两个元素
    nums6 = [1, 2]
    print(f"\n测试6（两个元素）:")
    print(f"输入: nums = {nums6}")
    result6 = sol.productExceptSelf(nums6)
    print(f"输出: {result6}")
    print(f"期望: [2, 1]")
    print(f"通过: {result6 == [2, 1]}")

    print("\n" + "=" * 60)
    print("所有测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    test()
