class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF   # 32비트 마스크
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # 임시 변수에 carry 저장
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        # a가 음수이면 보정
        return a if a <= MAX_INT else ~(a ^ MASK)