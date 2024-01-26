from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        
        # for i in nums:
        #     if i in freq:
        #         freq[i] += 1
        #     else:
        #         freq[i] = 1

        # ordered = sorted(freq.items(), key=lambda x:x[1], reverse=True)

        # return list(map(lambda x:x[0], ordered[:k]))

        freq = [(val, f) for val, f in Counter(nums).items()]
        ordered = sorted(freq, key=lambda x:x[1], reverse=True)
        return list(map(lambda x:x[0], ordered[:k]))
    
if __name__ == "__main__":
    test = Solution()

    print(test.topKFrequent([1,1,1,2,2,3], 2))