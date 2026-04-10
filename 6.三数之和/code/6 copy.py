
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sort_nums = sorted(nums)
        result = []
        for i,num in enumerate(sort_nums):
            left  = i+1
            right = len(nums)-1
            # 去除重复结果
            while(right>left):
                three_sum = num+sort_nums[left]+sort_nums[right]
                if(three_sum==0):
                    chack = [num,sort_nums[left],sort_nums[right]]
                    if chack not in result:
                        result.append(chack)
                    right -= 1
                    left +=1
                    continue
                while(three_sum>0 and right>left):
                    right -= 1
                    three_sum = num+sort_nums[left]+sort_nums[right]
                while(three_sum<0 and right>left):
                    left +=1
                    three_sum = num+sort_nums[left]+sort_nums[right]

        return result

        
a = Solution()
nums =[-1,0,1,2,-1,-4]       
print(a.threeSum(nums))