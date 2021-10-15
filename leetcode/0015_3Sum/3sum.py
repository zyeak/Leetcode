# Solution 1:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s <0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l <r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return result

# Solution 2:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        #1. Split nums into three list: negative, positve and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
                
        #2. Create separate set for negative and positive for O(1) look-up times
        N, P = set(n), set(p)
        
        #3. If there is at least 1 zeros in the list, add all case where -num exits in N and num exits in P
        if z:
            for num in P:
                if -1*num in N:
                    result.add((-1*num, 0, num))
                    
        #4. if there are at least 3 zeros in the list then include (0, 0, 0) = 0
        if len(z) >= 3:
            result.add((0, 0, 0))
            
        #5. For all pairs of negaive numbers(-3, -1) check to see if their complement (4)
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    result.add(tuple(sorted([n[i], n[j], target])))
                    
        #6. For all pairs of positive numbers(1, 1), check to see if their complement (-2) exits in the negative number set
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    result.add(tuple(sorted([p[i], p[j], target])))
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    print(s.threeSum([]))
    print(s.threeSum([0]))