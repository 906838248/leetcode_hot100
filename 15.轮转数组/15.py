from typing import List
import math


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        轮转数组 - 三次翻转法（推荐）

        时间复杂度：O(n)
        空间复杂度：O(1)

        算法思想：
          1. 整体翻转
          2. 翻转前 k 个元素
          3. 翻转后 n-k 个元素
        """
        n = len(nums)
        if n == 0:
            return

        k = k % n
        if k == 0:
            return

        def reverse(left: int, right: int) -> None:
            """翻转 nums[left..right]"""
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


def test():
    sol = Solution()

    print("=" * 60)
    print("轮转数组测试")
    print("=" * 60)

    # 示例1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    print(f"\n示例1:")
    print(f"输入: nums = {nums1}, k = 3")
    sol.rotate(nums1, 3)
    print(f"输出: {nums1}")
    print(f"期望: [5, 6, 7, 1, 2, 3, 4]")
    print(f"通过: {nums1 == [5, 6, 7, 1, 2, 3, 4]}")

    # 示例2
    nums2 = [-1, -100, 3, 99]
    print(f"\n示例2:")
    print(f"输入: nums = {nums2}, k = 2")
    sol.rotate(nums2, 2)
    print(f"输出: {nums2}")
    print(f"期望: [3, 99, -1, -100]")
    print(f"通过: {nums2 == [3, 99, -1, -100]}")

    # 测试3：k 大于数组长度
    nums3 = [1, 2, 3]
    print(f"\n测试3（k>n）:")
    print(f"输入: nums = {nums3}, k = 5")
    sol.rotate(nums3, 5)
    print(f"输出: {nums3}")
    print(f"期望: [2, 3, 1]")
    print(f"通过: {nums3 == [2, 3, 1]}")

    # 测试4：k = 0
    nums4 = [1, 2, 3]
    print(f"\n测试4（k=0）:")
    print(f"输入: nums = {nums4}, k = 0")
    sol.rotate(nums4, 0)
    print(f"输出: {nums4}")
    print(f"期望: [1, 2, 3]")
    print(f"通过: {nums4 == [1, 2, 3]}")

    # 测试5：单元素数组
    nums5 = [1]
    print(f"\n测试5（单元素）:")
    print(f"输入: nums = {nums5}, k = 3")
    sol.rotate(nums5, 3)
    print(f"输出: {nums5}")
    print(f"期望: [1]")
    print(f"通过: {nums5 == [1]}")

    # 测试6：k = n
    nums6 = [1, 2, 3, 4]
    print(f"\n测试6（k=n）:")
    print(f"输入: nums = {nums6}, k = 4")
    sol.rotate(nums6, 4)
    print(f"输出: {nums6}")
    print(f"期望: [1, 2, 3, 4]")
    print(f"通过: {nums6 == [1, 2, 3, 4]}")

    print("\n" + "=" * 60)
    print("所有测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    test()
