# Valid Anagram
def solution(s: str, t:str) -> bool:
    s_dict = {}
    
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else: s_dict[c] = 1
        
    for c in t:
        if c in s_dict:
            s_dict[c] -= 1
            if s_dict[c] == 0:
                del s_dict[c]
        else:
            return False
            
    return len(list(s_dict.items())) == 0