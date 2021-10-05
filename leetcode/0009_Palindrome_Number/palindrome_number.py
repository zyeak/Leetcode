# solution1
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        tmp, rev = x, 0
        
        while tmp != 0:
            rev *= 10
            rev += tmp%10
            tmp //= 10
        
        return x == rev

# solution1-1
class Solution1_1:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x>0 and x%10==0):
            return False
        
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
            
        return  x == rev or x == rev // 10

# solution 2:
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if(str_x == str_x[::-1]):
            return True
        return False
