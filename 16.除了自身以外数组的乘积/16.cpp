#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return {};
        }

        vector<int> answer(n, 1);

        int left = 1;
        for (int i = 0; i < n; i++) {
            answer[i] = left;
            left *= nums[i];
        }

        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= right;
            right *= nums[i];
        }

        return answer;
    }
};

void test() {
    Solution sol;

    cout << "============================================================" << endl;
    cout << "除自身以外数组的乘积测试" << endl;
    cout << "============================================================" << endl;

    // 示例1
    vector<int> nums1 = {1, 2, 3, 4};
    cout << "\n示例1:" << endl;
    cout << "输入: nums = [1,2,3,4]" << endl;
    vector<int> result1 = sol.productExceptSelf(nums1);
    cout << "输出: [";
    for (int i = 0; i < result1.size(); i++) {
        cout << result1[i];
        if (i < result1.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [24, 12, 8, 6]" << endl;
    vector<int> expected1 = {24, 12, 8, 6};
    cout << "通过: " << (result1 == expected1 ? "true" : "false") << endl;

    // 示例2
    vector<int> nums2 = {-1, 1, 0, -3, 3};
    cout << "\n示例2:" << endl;
    cout << "输入: nums = [-1,1,0,-3,3]" << endl;
    vector<int> result2 = sol.productExceptSelf(nums2);
    cout << "输出: [";
    for (int i = 0; i < result2.size(); i++) {
        cout << result2[i];
        if (i < result2.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [0, 0, 9, 0, 0]" << endl;
    vector<int> expected2 = {0, 0, 9, 0, 0};
    cout << "通过: " << (result2 == expected2 ? "true" : "false") << endl;

    // 测试3：包含负数
    vector<int> nums3 = {-1, -2, -3, -4};
    cout << "\n测试3（全是负数）:" << endl;
    cout << "输入: nums = [-1,-2,-3,-4]" << endl;
    vector<int> result3 = sol.productExceptSelf(nums3);
    cout << "输出: [";
    for (int i = 0; i < result3.size(); i++) {
        cout << result3[i];
        if (i < result3.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [-24, -12, -8, -6]" << endl;
    vector<int> expected3 = {-24, -12, -8, -6};
    cout << "通过: " << (result3 == expected3 ? "true" : "false") << endl;

    // 测试4：包含零
    vector<int> nums4 = {0, 2, 3, 4};
    cout << "\n测试4（包含零）:" << endl;
    cout << "输入: nums = [0,2,3,4]" << endl;
    vector<int> result4 = sol.productExceptSelf(nums4);
    cout << "输出: [";
    for (int i = 0; i < result4.size(); i++) {
        cout << result4[i];
        if (i < result4.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [24, 0, 0, 0]" << endl;
    vector<int> expected4 = {24, 0, 0, 0};
    cout << "通过: " << (result4 == expected4 ? "true" : "false") << endl;

    // 测试5：多个零
    vector<int> nums5 = {0, 0, 2, 3};
    cout << "\n测试5（多个零）:" << endl;
    cout << "输入: nums = [0,0,2,3]" << endl;
    vector<int> result5 = sol.productExceptSelf(nums5);
    cout << "输出: [";
    for (int i = 0; i < result5.size(); i++) {
        cout << result5[i];
        if (i < result5.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [0, 0, 0, 0]" << endl;
    vector<int> expected5 = {0, 0, 0, 0};
    cout << "通过: " << (result5 == expected5 ? "true" : "false") << endl;

    // 测试6：两个元素
    vector<int> nums6 = {1, 2};
    cout << "\n测试6（两个元素）:" << endl;
    cout << "输入: nums = [1,2]" << endl;
    vector<int> result6 = sol.productExceptSelf(nums6);
    cout << "输出: [";
    for (int i = 0; i < result6.size(); i++) {
        cout << result6[i];
        if (i < result6.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [2, 1]" << endl;
    vector<int> expected6 = {2, 1};
    cout << "通过: " << (result6 == expected6 ? "true" : "false") << endl;

    cout << "\n============================================================" << endl;
    cout << "所有测试完成！" << endl;
    cout << "============================================================" << endl;
}

int main() {
    test();
    return 0;
}
