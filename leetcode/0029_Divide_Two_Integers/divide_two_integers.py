# Bitwise solution
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor <0)
        divisor, dividend = abs(divisor), abs(dividend)
        
        quotient = 0
        total = divisor
        
        while total <= dividend:
            current_quotient = 1
            while (total << 1) <= dividend:
                total <<= 1
                current_quotient <<= 1
            dividend -= total
            total = divisor
            quotient += current_quotient
        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))