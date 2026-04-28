#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return;
        }

        int m = matrix.size();
        int n = matrix[0].size();

        bool first_row_has_zero = false;
        bool first_col_has_zero = false;

        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                first_row_has_zero = true;
                break;
            }
        }

        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                first_col_has_zero = true;
                break;
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (first_row_has_zero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

        if (first_col_has_zero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
};

void printMatrix(const vector<vector<int>>& matrix) {
    cout << "[";
    for (int i = 0; i < matrix.size(); i++) {
        if (i > 0) cout << " ";
        cout << "[";
        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j];
            if (j < matrix[i].size() - 1) cout << ", ";
        }
        cout << "]";
        if (i < matrix.size() - 1) cout << "," << endl;
    }
    cout << "]" << endl;
}

void test() {
    Solution sol;

    cout << "============================================================" << endl;
    cout << "矩阵置零测试" << endl;
    cout << "============================================================" << endl;

    // 示例1
    vector<vector<int>> matrix1 = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    cout << "\n示例1:" << endl;
    cout << "输入: ";
    printMatrix(matrix1);
    sol.setZeroes(matrix1);
    cout << "输出: ";
    printMatrix(matrix1);
    cout << "期望: [[1,0,1],[0,0,0],[1,0,1]]" << endl;
    vector<vector<int>> expected1 = {{1, 0, 1}, {0, 0, 0}, {1, 0, 1}};
    cout << "通过: " << (matrix1 == expected1 ? "true" : "false") << endl;

    // 示例2
    vector<vector<int>> matrix2 = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
    cout << "\n示例2:" << endl;
    cout << "输入: ";
    printMatrix(matrix2);
    sol.setZeroes(matrix2);
    cout << "输出: ";
    printMatrix(matrix2);
    cout << "期望: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]" << endl;
    vector<vector<int>> expected2 = {{0, 0, 0, 0}, {0, 4, 5, 0}, {0, 3, 1, 0}};
    cout << "通过: " << (matrix2 == expected2 ? "true" : "false") << endl;

    // 测试3：只有一行
    vector<vector<int>> matrix3 = {{1, 0, 1}};
    cout << "\n测试3（只有一行）:" << endl;
    cout << "输入: ";
    printMatrix(matrix3);
    sol.setZeroes(matrix3);
    cout << "输出: ";
    printMatrix(matrix3);
    cout << "期望: [[0,0,0]]" << endl;
    vector<vector<int>> expected3 = {{0, 0, 0}};
    cout << "通过: " << (matrix3 == expected3 ? "true" : "false") << endl;

    // 测试4：只有一列
    vector<vector<int>> matrix4 = {{1}, {0}, {1}};
    cout << "\n测试4（只有一列）:" << endl;
    cout << "输入: ";
    printMatrix(matrix4);
    sol.setZeroes(matrix4);
    cout << "输出: ";
    printMatrix(matrix4);
    cout << "期望: [[0],[0],[0]]" << endl;
    vector<vector<int>> expected4 = {{0}, {0}, {0}};
    cout << "通过: " << (matrix4 == expected4 ? "true" : "false") << endl;

    // 测试5：没有零
    vector<vector<int>> matrix5 = {{1, 2, 3}, {4, 5, 6}};
    cout << "\n测试5（没有零）:" << endl;
    cout << "输入: ";
    printMatrix(matrix5);
    sol.setZeroes(matrix5);
    cout << "输出: ";
    printMatrix(matrix5);
    cout << "期望: [[1,2,3],[4,5,6]]" << endl;
    vector<vector<int>> expected5 = {{1, 2, 3}, {4, 5, 6}};
    cout << "通过: " << (matrix5 == expected5 ? "true" : "false") << endl;

    // 测试6：左上角是零
    vector<vector<int>> matrix6 = {{0, 1}, {1, 1}};
    cout << "\n测试6（左上角是零）:" << endl;
    cout << "输入: ";
    printMatrix(matrix6);
    sol.setZeroes(matrix6);
    cout << "输出: ";
    printMatrix(matrix6);
    cout << "期望: [[0,0],[0,1]]" << endl;
    vector<vector<int>> expected6 = {{0, 0}, {0, 1}};
    cout << "通过: " << (matrix6 == expected6 ? "true" : "false") << endl;

    cout << "\n============================================================" << endl;
    cout << "所有测试完成！" << endl;
    cout << "============================================================" << endl;
}

int main() {
    test();
    return 0;
}
