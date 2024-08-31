def solution(self, strs: list[str]) -> list[list[str]]:
    tmp_groups: list[tuple[int, dict[str, str], list[str]]] = []
    
    for s in strs:
        letters = Counter(s)
        
        matching_index = -1
        
        for i in range(0, len(tmp_groups)):
            if len(s) == tmp_groups[i][0] and tmp_groups[i][1] == letters:
                matching_index = i
                
        if matching_index >= 0:
            tmp_groups[matching_index][2].append(s)
        else:
            tmp_groups.append((len(s), letters, [s]))
            
    return [group[2] for group in tmp_groups]