# Contains Duplicate
def solution(nums: list[int]) -> bool:
	found = {}
    for num in nums:
        if num in found:
            return True
        else:
            found[num] = True
            
    return False