class Solution:
    def myAtoi(self, s: str) -> int:
        INTMAX = 2147483647
        INTMIN = -2147483648
        str = s.strip()
        if not str:
            return 0
        sign, i = 1, 0
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1
        num = 0
        while i < len(str):
            if not str[i].isdigit():
                break
            num = num*10 + ord(str[i]) - ord('0')
            i += 1
        num = num * sign
        return max(INTMIN, min(num, INTMAX))
        

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))