class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        def decrement_item(map, val):
            if map[val] == 1:
                del map[val]
            else:
                map[val] -= 1

        # convert s1 to a dict
        s1_vals = {}
        for c in s1:
            if c in s1_vals:
                s1_vals[c] += 1
            else:
                s1_vals[c] = 1

        for i in range(len(s2) - len(s1) + 1):
            if s2[i] in s1_vals:
                tmp = deepcopy(s1_vals)
                perm = True
                while i < len(s2):
                    if len(tmp.items()) == 0:
                        break
                    if s2[i] in tmp:
                        decrement_item(tmp, s2[i])
                    else:
                        perm = False
                        break
                    i += 1

                if perm:
                    return True
        
        return False
