class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        if(len(nums)) == 0:
            return length
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length