#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefix_count;
        prefix_count[0] = 1;
        int prefix = 0;
        int result = 0;
        int n = nums.size();
        for (int i  : nums) {
            prefix += i;
            if (prefix_count.find(prefix-k)!=prefix_count.end()) {
                result += prefix_count[prefix-k];         
            }
            prefix_count[prefix]++;
        
        }
        return result;
    }
};