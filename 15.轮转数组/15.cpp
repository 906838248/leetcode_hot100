#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return;

        k = k % n;
        if (k == 0) return;

        auto reverse = [&](int left, int right) {
            while (left < right) {
                swap(nums[left], nums[right]);
                left++;
                right--;
            }
        };

        reverse(0, n - 1);
        reverse(0, k - 1);
        reverse(k, n - 1);
    }
};

void test() {
    Solution sol;

    cout << "============================================================" << endl;
    cout << "轮转数组测试" << endl;
    cout << "============================================================" << endl;

    // 示例1
    vector<int> nums1 = {1, 2, 3, 4, 5, 6, 7};
    cout << "\n示例1:" << endl;
    cout << "输入: nums = [1,2,3,4,5,6,7], k = 3" << endl;
    sol.rotate(nums1, 3);
    cout << "输出: [";
    for (int i = 0; i < nums1.size(); i++) {
        cout << nums1[i];
        if (i < nums1.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [5, 6, 7, 1, 2, 3, 4]" << endl;
    vector<int> expected1 = {5, 6, 7, 1, 2, 3, 4};
    cout << "通过: " << (nums1 == expected1 ? "true" : "false") << endl;

    // 示例2
    vector<int> nums2 = {-1, -100, 3, 99};
    cout << "\n示例2:" << endl;
    cout << "输入: nums = [-1,-100,3,99], k = 2" << endl;
    sol.rotate(nums2, 2);
    cout << "输出: [";
    for (int i = 0; i < nums2.size(); i++) {
        cout << nums2[i];
        if (i < nums2.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [3, 99, -1, -100]" << endl;
    vector<int> expected2 = {3, 99, -1, -100};
    cout << "通过: " << (nums2 == expected2 ? "true" : "false") << endl;

    // 测试3：k 大于数组长度
    vector<int> nums3 = {1, 2, 3};
    cout << "\n测试3（k>n）:" << endl;
    cout << "输入: nums = [1,2,3], k = 5" << endl;
    sol.rotate(nums3, 5);
    cout << "输出: [";
    for (int i = 0; i < nums3.size(); i++) {
        cout << nums3[i];
        if (i < nums3.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [2, 3, 1]" << endl;
    vector<int> expected3 = {2, 3, 1};
    cout << "通过: " << (nums3 == expected3 ? "true" : "false") << endl;

    // 测试4：k = 0
    vector<int> nums4 = {1, 2, 3};
    cout << "\n测试4（k=0）:" << endl;
    cout << "输入: nums = [1,2,3], k = 0" << endl;
    sol.rotate(nums4, 0);
    cout << "输出: [";
    for (int i = 0; i < nums4.size(); i++) {
        cout << nums4[i];
        if (i < nums4.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [1, 2, 3]" << endl;
    vector<int> expected4 = {1, 2, 3};
    cout << "通过: " << (nums4 == expected4 ? "true" : "false") << endl;

    // 测试5：单元素数组
    vector<int> nums5 = {1};
    cout << "\n测试5（单元素）:" << endl;
    cout << "输入: nums = [1], k = 3" << endl;
    sol.rotate(nums5, 3);
    cout << "输出: [";
    for (int i = 0; i < nums5.size(); i++) {
        cout << nums5[i];
        if (i < nums5.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [1]" << endl;
    vector<int> expected5 = {1};
    cout << "通过: " << (nums5 == expected5 ? "true" : "false") << endl;

    // 测试6：k = n
    vector<int> nums6 = {1, 2, 3, 4};
    cout << "\n测试6（k=n）:" << endl;
    cout << "输入: nums = [1,2,3,4], k = 4" << endl;
    sol.rotate(nums6, 4);
    cout << "输出: [";
    for (int i = 0; i < nums6.size(); i++) {
        cout << nums6[i];
        if (i < nums6.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    cout << "期望: [1, 2, 3, 4]" << endl;
    vector<int> expected6 = {1, 2, 3, 4};
    cout << "通过: " << (nums6 == expected6 ? "true" : "false") << endl;

    cout << "\n============================================================" << endl;
    cout << "所有测试完成！" << endl;
    cout << "============================================================" << endl;
}

int main() {
    test();
    return 0;
}
