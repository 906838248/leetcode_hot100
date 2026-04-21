#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current_num=0,max_num=INT16_MIN;
        for(int i =0;i<nums.size();i++)
        {
            if((current_num+nums[i])<nums[i]){
                current_num=nums[i];
            }
            else {
                current_num += nums[i];
            }
            if(current_num>max_num){
                max_num = current_num;
            }
        }
        return max_num;
    }
};