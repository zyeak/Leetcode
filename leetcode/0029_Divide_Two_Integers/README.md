# [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

## Problems:
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator. <br>

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2. <br>

Return the quotient after dividing dividend by divisor. <br>

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31. <br>

### Example 1:
Input: dividend = 10, divisor = 3 <br>
Output: 3 <br>
Explanation: 10/3 = 3.33333.. which is truncated to 3. <br>

### Example 2:
Input: dividend = 7, divisor = -3 <br>
Output: -2 <br>
Explanation: 7/-3 = -2.33333.. which is truncated to -2. <br>

### Example 3:
Input: dividend = 0, divisor = 1 <br>
Output: 0 <br>

### Constraints:
* -2^31 <= dividend, divisor <= 2^31 - 1
* divisor != 0


