#include <vector>
#include <algorithm>

class Solution {
public:
    /**
     * 三数之和 - 排序 + 双指针法
     * 
     * 时间复杂度：O(n²)
     * 空间复杂度：O(1)
     */
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        int n = nums.size();
        
        if (n < 3) {
            return result;
        }
        
        // 排序
        std::sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n - 2; i++) {
            // 跳过重复
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // 剪枝
            if (nums[i] + nums[i + 1] + nums[i + 2] > 0) {
                break;
            }
            
            if (nums[i] + nums[n - 1] + nums[n - 2] < 0) {
                continue;
            }
            
            // 双指针
            int left = i + 1;
            int right = n - 1;
            
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                
                if (total == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
                    left++;
                    right--;
                }
                else if (total < 0) {
                    left++;
                }
                else {
                    right--;
                }
            }
        }
        
        return result;
    }
};