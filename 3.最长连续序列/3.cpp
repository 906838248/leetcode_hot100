#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()) return 0;
        unordered_set<int> num_set(nums.begin(), nums.end());
        int max_count=1;
        int count = 1;
        for (int num : num_set) {
            if(num_set.find(num-1)==num_set.end()){
                int now_num = num;
                while (num_set.find(now_num+1)!=num_set.end()) {
                    count ++;
                    now_num ++;
                }
            }
            if(count>max_count) max_count=count;
            count = 1;
        }
        return max_count;
    }
};