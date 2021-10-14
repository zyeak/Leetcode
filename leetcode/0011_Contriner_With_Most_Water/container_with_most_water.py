class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, area, result = 0, len(height)-1, 0, 0
        
        while left < right:
            area = (right-left) * min(height[left], height[right])
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))