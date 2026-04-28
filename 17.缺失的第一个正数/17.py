from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        缺失的第一个正数 - 原地哈希法

        时间复杂度：O(n)
        空间复杂度：O(1)

        算法思想：
          1. 将数字 k 放到索引 k-1 的位置
          2. 遍历数组，将符合条件的数字放到正确位置
          3. 再次遍历，找到第一个位置 i 不是 i+1 的
        """
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


def test():
    sol = Solution()

    print("=" * 60)
    print("缺失的第一个正数测试")
    print("=" * 60)

    # 示例1
    nums1 = [1, 2, 0]
    print(f"\n示例1:")
    print(f"输入: nums = {nums1}")
    result1 = sol.firstMissingPositive(nums1)
    print(f"输出: {result1}")
    print(f"期望: 3")
    print(f"通过: {result1 == 3}")

    # 示例2
    nums2 = [3, 4, -1, 1]
    print(f"\n示例2:")
    print(f"输入: nums = {nums2}")
    result2 = sol.firstMissingPositive(nums2)
    print(f"输出: {result2}")
    print(f"期望: 2")
    print(f"通过: {result2 == 2}")

    # 示例3
    nums3 = [7, 8, 9, 11, 12]
    print(f"\n示例3:")
    print(f"输入: nums = {nums3}")
    result3 = sol.firstMissingPositive(nums3)
    print(f"输出: {result3}")
    print(f"期望: 1")
    print(f"通过: {result3 == 1}")

    # 测试4：包含重复数字
    nums4 = [1, 1, 0, 2]
    print(f"\n测试4（包含重复）:")
    print(f"输入: nums = {nums4}")
    result4 = sol.firstMissingPositive(nums4)
    print(f"输出: {result4}")
    print(f"期望: 3")
    print(f"通过: {result4 == 3}")

    # 测试5：全负数
    nums5 = [-1, -2, -3]
    print(f"\n测试5（全负数）:")
    print(f"输入: nums = {nums5}")
    result5 = sol.firstMissingPositive(nums5)
    print(f"输出: {result5}")
    print(f"期望: 1")
    print(f"通过: {result5 == 1}")

    # 测试6：已经是连续的
    nums6 = [1, 2, 3, 4, 5]
    print(f"\n测试6（已连续）:")
    print(f"输入: nums = {nums6}")
    result6 = sol.firstMissingPositive(nums6)
    print(f"输出: {result6}")
    print(f"期望: 6")
    print(f"通过: {result6 == 6}")

    # 测试7：两个元素
    nums7 = [2, 2]
    print(f"\n测试7（两相同元素）:")
    print(f"输入: nums = {nums7}")
    result7 = sol.firstMissingPositive(nums7)
    print(f"输出: {result7}")
    print(f"期望: 1")
    print(f"通过: {result7 == 1}")

    print("\n" + "=" * 60)
    print("所有测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    test()
