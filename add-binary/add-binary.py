class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # carry is remainder
        carry = 0
        # build result
        result = ''
        # convert to lists
        a = list(a)
        b = list(b)
        # while digits remain
        while a or b or carry:
            # add both to carry
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            # build result
            result += str(carry %2)
            carry //= 2
        # reverse order
        return result[::-1]