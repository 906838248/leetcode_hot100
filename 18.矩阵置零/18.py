from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        矩阵置零 - 原地算法

        时间复杂度：O(m*n)
        空间复杂度：O(1)

        算法思想：
          1. 用第一行和第一列作为标记
          2. 先处理内部元素，再处理第一行和第一列
        """
        if not matrix or not matrix[0]:
            return

        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0


def test():
    sol = Solution()

    print("=" * 60)
    print("矩阵置零测试")
    print("=" * 60)

    # 示例1
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(f"\n示例1:")
    print(f"输入: {matrix1}")
    sol.setZeroes(matrix1)
    print(f"输出: {matrix1}")
    print(f"期望: [[1,0,1],[0,0,0],[1,0,1]]")
    print(f"通过: {matrix1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]}")

    # 示例2
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(f"\n示例2:")
    print(f"输入: {matrix2}")
    sol.setZeroes(matrix2)
    print(f"输出: {matrix2}")
    print(f"期望: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]")
    print(f"通过: {matrix2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]}")

    # 测试3：只有一行
    matrix3 = [[1, 0, 1]]
    print(f"\n测试3（只有一行）:")
    print(f"输入: {matrix3}")
    sol.setZeroes(matrix3)
    print(f"输出: {matrix3}")
    print(f"期望: [[0, 0, 0]]")
    print(f"通过: {matrix3 == [[0, 0, 0]]}")

    # 测试4：只有一列
    matrix4 = [[1], [0], [1]]
    print(f"\n测试4（只有一列）:")
    print(f"输入: {matrix4}")
    sol.setZeroes(matrix4)
    print(f"输出: {matrix4}")
    print(f"期望: [[0], [0], [0]]")
    print(f"通过: {matrix4 == [[0], [0], [0]]}")

    # 测试5：没有零
    matrix5 = [[1, 2, 3], [4, 5, 6]]
    print(f"\n测试5（没有零）:")
    print(f"输入: {matrix5}")
    sol.setZeroes(matrix5)
    print(f"输出: {matrix5}")
    print(f"期望: [[1,2,3],[4,5,6]]")
    print(f"通过: {matrix5 == [[1, 2, 3], [4, 5, 6]]}")

    # 测试6：左上角是零
    matrix6 = [[0, 1], [1, 1]]
    print(f"\n测试6（左上角是零）:")
    print(f"输入: {matrix6}")
    sol.setZeroes(matrix6)
    print(f"输出: {matrix6}")
    print(f"期望: [[0,0],[0,1]]")
    print(f"通过: {matrix6 == [[0, 0], [0, 1]]}")

    print("\n" + "=" * 60)
    print("所有测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    test()
