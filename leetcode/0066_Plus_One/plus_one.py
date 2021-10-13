# solution1: recursive
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits

# solution2:
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 1:
            if digits[0] < 9:
                digits[0] += 1
                return digits
            else:
                return [1,0]

        loc = n-1
        while digits[loc] + 1 == 10 and loc >= 0:
            digits[loc] = 0
            loc -= 1
            
        if loc >= 0:
            digits[loc] += 1
            return digits
        else:
            return [1] + digits

# solution3:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int, list(str(int(''.join(map(str, digits))) +1)))

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))