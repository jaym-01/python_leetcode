from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0
        out: List[int] = []

        for i in nums:
            if i == 0:
                zeroes += 1
            else:
                prod *= i
        
        for i in nums:
            if zeroes > 1:
                out.append(0)
            elif zeroes == 1:
                if i == 0:
                    out.append(int(prod))
                else:
                    out.append(0)
            else:
                out.append(int(prod/i))
        
        return out
    
if __name__ == "__main__":
    test = Solution()

    print(test.productExceptSelf([1, 2, 3, 4]))