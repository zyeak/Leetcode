# Solution1: based on three sum
class Solution(object):
  def threeSum(self, nums, target):
    results = []
    nums.sort()
    for i in range(len(nums)-2):
      l = i + 1; r = len(nums) - 1
      t = target - nums[i]
      if i == 0 or nums[i] != nums[i-1]:
        while l < r:
          s = nums[l] + nums[r]
          if s == t:
            results.append([nums[i], nums[l], nums[r]])
            while l < r and nums[l] == nums[l+1]: l += 1
            while l < r and nums[r] == nums[r-1]: r -= 1
            l += 1; r -=1
          elif s < t:
            l += 1
          else:
            r -= 1

    return results

  def fourSum(self, nums, target):
    results = []
    nums.sort()
    for i in range(len(nums)-3):
      if i == 0 or nums[i] != nums[i-1]:
        threeResult = self.threeSum(nums[i+1:], target-nums[i])
        for item in threeResult:
          results.append([nums[i]] + item)
    return results

# Solution 2: two Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)
        
        
    def kSum(self, nums:List[int], target:int, N:int) -> List[List[int]]:
        result = []
        if not nums:
            return result
        
        average_value = target // N
        
        if average_value < nums[0] or nums[-1] < average_value:
            return result
        
        if N == 2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subset in self.kSum(nums[i+1:], target-nums[i], N-1):
                    result.append([nums[i]]+subset)
        return result
        
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        s = set()
        
        for i in range(len(nums)):
            if len(result) == 0 or result[-1][1] != nums[i]:
                if target - nums[i] in s:
                    result. append([target-nums[i], nums[i]])
            s.add(nums[i])
            
        return result
                