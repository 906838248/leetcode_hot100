#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    /**
     * 在数组中找出两个和为目标值的整数，返回它们的数组下标
     * 
     * @param nums 整数数组
     * @param target 目标值
     * @return 两个整数下标组成的向量
     */
    vector<int> twoSum(vector<int>& nums, int target) {
        // 创建哈希表：存储 {数值: 索引}
        unordered_map<int, int> hashmap;
        
        // 遍历数组（需要索引）
        for (int i = 0; i < nums.size(); i++) {
            // 计算需要的另一个数
            int complement = target - nums[i];
            
            // 检查 complement 是否在哈希表中
            if (hashmap.find(complement) != hashmap.end()) {
                // 找到了！返回两个索引
                return {hashmap[complement], i};
            }
            
            // 没找到，将当前元素存入哈希表
            hashmap[nums[i]] = i;
        }
        
        // 没有找到答案
        return {};
    }
};

int main() {
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> result = solution.twoSum(nums, target);
    
    if (!result.empty()) {
        cout << "找到答案：[" << result[0] << ", " << result[1] << "]" << endl;
    }
    
    return 0;
}