from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n =len(height) - 1
        if(n<2) : return 0 
        result = 0
        for curreet in range(1,n):
            left_height = height[:curreet]
            left_max = max(left_height)
            if (left_max<height[curreet]): continue

            right_height = height[curreet+1:]
            right_max = max(right_height)
            if(right_max<height[curreet]) : continue
            result +=min(right_max,left_max) - height[curreet]
        return result


s=Solution()
a=[0,1,0,2,1,0,1,3,2,1,2,1]
s.trap(a)