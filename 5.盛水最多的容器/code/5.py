# 前后指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        max_water = 0
        right = len(height)-1
        while(left<right):
            water = (right - left) *min(height[right],height[left])
            if(water>max_water):
                max_water = water
        
            if(height[right]>height[left]):
                left +=1
            else:
                right -= 1
        return max_water
