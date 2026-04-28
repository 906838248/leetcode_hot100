#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            while (1 <= nums[i] && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                swap(nums[i], nums[nums[i] - 1]);
            }
        }

        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        return n + 1;
    }
};

void test() {
    Solution sol;

    cout << "============================================================" << endl;
    cout << "缺失的第一个正数测试" << endl;
    cout << "============================================================" << endl;

    // 示例1
    vector<int> nums1 = {1, 2, 0};
    cout << "\n示例1:" << endl;
    cout << "输入: nums = [1,2,0]" << endl;
    int result1 = sol.firstMissingPositive(nums1);
    cout << "输出: " << result1 << endl;
    cout << "期望: 3" << endl;
    cout << "通过: " << (result1 == 3 ? "true" : "false") << endl;

    // 示例2
    vector<int> nums2 = {3, 4, -1, 1};
    cout << "\n示例2:" << endl;
    cout << "输入: nums = [3,4,-1,1]" << endl;
    int result2 = sol.firstMissingPositive(nums2);
    cout << "输出: " << result2 << endl;
    cout << "期望: 2" << endl;
    cout << "通过: " << (result2 == 2 ? "true" : "false") << endl;

    // 示例3
    vector<int> nums3 = {7, 8, 9, 11, 12};
    cout << "\n示例3:" << endl;
    cout << "输入: nums = [7,8,9,11,12]" << endl;
    int result3 = sol.firstMissingPositive(nums3);
    cout << "输出: " << result3 << endl;
    cout << "期望: 1" << endl;
    cout << "通过: " << (result3 == 1 ? "true" : "false") << endl;

    // 测试4：包含重复数字
    vector<int> nums4 = {1, 1, 0, 2};
    cout << "\n测试4（包含重复）:" << endl;
    cout << "输入: nums = [1,1,0,2]" << endl;
    int result4 = sol.firstMissingPositive(nums4);
    cout << "输出: " << result4 << endl;
    cout << "期望: 3" << endl;
    cout << "通过: " << (result4 == 3 ? "true" : "false") << endl;

    // 测试5：全负数
    vector<int> nums5 = {-1, -2, -3};
    cout << "\n测试5（全负数）:" << endl;
    cout << "输入: nums = [-1,-2,-3]" << endl;
    int result5 = sol.firstMissingPositive(nums5);
    cout << "输出: " << result5 << endl;
    cout << "期望: 1" << endl;
    cout << "通过: " << (result5 == 1 ? "true" : "false") << endl;

    // 测试6：已经是连续的
    vector<int> nums6 = {1, 2, 3, 4, 5};
    cout << "\n测试6（已连续）:" << endl;
    cout << "输入: nums = [1,2,3,4,5]" << endl;
    int result6 = sol.firstMissingPositive(nums6);
    cout << "输出: " << result6 << endl;
    cout << "期望: 6" << endl;
    cout << "通过: " << (result6 == 6 ? "true" : "false") << endl;

    // 测试7：两个元素
    vector<int> nums7 = {2, 2};
    cout << "\n测试7（两相同元素）:" << endl;
    cout << "输入: nums = [2,2]" << endl;
    int result7 = sol.firstMissingPositive(nums7);
    cout << "输出: " << result7 << endl;
    cout << "期望: 1" << endl;
    cout << "通过: " << (result7 == 1 ? "true" : "false") << endl;

    cout << "\n============================================================" << endl;
    cout << "所有测试完成！" << endl;
    cout << "============================================================" << endl;
}

int main() {
    test();
    return 0;
}
