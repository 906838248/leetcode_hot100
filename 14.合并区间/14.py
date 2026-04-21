from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并区间

        时间复杂度：O(n log n)
        空间复杂度：O(1) （不计输出空间）

        算法步骤：
            1. 按区间的起始位置排序
            2. 遍历区间，合并重叠的区间
            3. 判断重叠：当前区间起始 ≤ 上一个合并区间结束
            4. 合并：更新合并区间的结束位置为较大值
        """
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            last_merged = merged[-1]

            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)

        return merged


def test():
    sol = Solution()

    # 示例1
    result1 = sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(f"示例1: {result1}")
    print(f"期望: [[1, 6], [8, 10], [15, 18]]")
    print(f"通过: {result1 == [[1, 6], [8, 10], [15, 18]]}\n")

    # 示例2
    result2 = sol.merge([[1, 4], [4, 5]])
    print(f"示例2: {result2}")
    print(f"期望: [[1, 5]]")
    print(f"通过: {result2 == [[1, 5]]}\n")

    # 示例3
    result3 = sol.merge([[4, 7], [1, 4]])
    print(f"示例3: {result3}")
    print(f"期望: [[1, 7]]")
    print(f"通过: {result3 == [[1, 7]]}\n")

    # 测试4：完全独立的区间
    result4 = sol.merge([[1, 2], [3, 4], [5, 6]])
    print(f"测试4（独立区间）: {result4}")
    print(f"期望: [[1, 2], [3, 4], [5, 6]]")
    print(f"通过: {result4 == [[1, 2], [3, 4], [5, 6]]}\n")

    # 测试5：包含关系
    result5 = sol.merge([[1, 10], [2, 3], [4, 5]])
    print(f"测试5（包含关系）: {result5}")
    print(f"期望: [[1, 10]]")
    print(f"通过: {result5 == [[1, 10]]}\n")

    # 测试6：完全重叠
    result6 = sol.merge([[1, 5], [2, 4], [3, 6]])
    print(f"测试6（完全重叠）: {result6}")
    print(f"期望: [[1, 6]]")
    print(f"通过: {result6 == [[1, 6]]}\n")

    # 测试7：单个区间
    result7 = sol.merge([[1, 3]])
    print(f"测试7（单个区间）: {result7}")
    print(f"期望: [[1, 3]]")
    print(f"通过: {result7 == [[1, 3]]}\n")


if __name__ == "__main__":
    test()
