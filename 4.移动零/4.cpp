
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0;
        int n = nums.size();
        for(int right=0;right<n;right++)
        {
            if(nums[right]!=0)
            {
                swap(nums[left], nums[right]);
                left++;
            }
        }
    }
};