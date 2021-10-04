# solution 1
class Solution:
    def reverse(self, x: int) -> int:
        result=0
        max_int = 2**31-1
        min_int = -2**31
        tmp = abs(x)

        while(tmp>0):
            result = result*10 + tmp%10
            tmp //= 10

        if x<0:
            result *= -1

        if result > max_int or result < min_int:
            return 0
            
        return result


# solution 2
class Solution:
    def reverse(self, x: int) -> int:
        signed = -1 if x<0 else 1
        result = int(str(x*signed)[::-1])*signed
        
        max_int = 2**31-1
        min_int = -2**31
        
        if(result<min_int) or (result>max_int):
            return 0
        
        return result