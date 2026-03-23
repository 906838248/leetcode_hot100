class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        在数组中找出两个和为目标值的整数，返回它们的数组下标

        使用哈希表实现，时间复杂度 O(n)，空间复杂度 O(n)

        Args:
            nums: 整数数组
            target: 目标值

        Returns:
            两个整数下标组成的数组，如果不存在则返回空数组
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

    


nums = [3, 3]
target = 6
a = Solution()
print(a.twoSum(nums, target))
