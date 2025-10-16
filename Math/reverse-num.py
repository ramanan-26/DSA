class Solution:
    def reverse(self, x: int) -> int:

        flag, result = False, 0
        if x < 0:
            x *= -1
            flag = True

        while (x > 0):
            lastDigit = x % 10
            result = lastDigit + (result * 10)
            x //= 10

        if flag:
            result = -1 * result

        # Check 32-bit signed integer overflow
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
