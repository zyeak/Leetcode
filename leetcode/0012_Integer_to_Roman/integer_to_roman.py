# Solution1:
class Solution1:
    def intToRoman(self, num: int) -> str:
        roman = {1000:'M',
                900:'CM',
                500:'D',
                400:'CD',
                100:'C',
                90:'XC',
                50:'L',
                40:'XL',
                10:'X',
                9:'IX',
                5:'V',
                4:'IV',
                1:'I'}
        result = ''
        for i in roman:
            result += roman[i] * (num // i)
            num %= i
        return result

# Solution2:
class Solution:
    def intToRoman(self, num: int) -> str: 
        result = ''
        M = {0:'', 1:'M', 2:'MM', 3:'MMM'}
        C = {0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
        X = {0:'', 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
        I = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
        
        result = M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]

        return result

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
