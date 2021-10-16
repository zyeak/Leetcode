# Solution: two-pointers
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            
            if i >0 and nums[i] == nums[i-1]:
                continue 
        
            left, right = i+1, len(nums)-1
            
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                
                if abs(cur - target) < abs(result - target):
                    result = cur
                
                if cur < target:
                    left += 1
                elif cur > target:
                    right -= 1
                else:
                    return result
        return result