class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = [(digits.pop(-1) + 1) % 10]

        carry = 1 if out[0] == 0 else 0

        while len(digits) > 0:
            top = digits.pop(-1)
            out.insert(0, (top + carry) % 10)
            carry = 1 if out[0] == 0 and top != 0 else 0
        
        if carry == 1:
            out.insert(0, 1)

        return out

