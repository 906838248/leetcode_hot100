#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int max_water = 0;
        int right = height.size() - 1;
        while(left<right)
        {
            int water = (right - left) * min(height[left],height[right]);
            if(water>max_water) max_water=water;
            if(height[left]>height[right]) right --;
            else left++;


        }
        return max_water;
    }
};