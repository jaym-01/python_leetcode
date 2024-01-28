class Solution:
    def myAtoi(self, s: str) -> int:
        
        start_flag = False
        num_str = ""
        num = 0

        for c in s:
            if not start_flag:
                if c == ' ':
                    continue
                elif c == '+' or ord(c) > 47 and ord(c) < 58 or c == '-':
                    start_flag = True
                    if c == '-':# what if you get minus / plus and nothing in the end
                        num_str += '-'
                    elif c != '+':
                        num_str += c
                else:
                    return 0
            else:
                if ord(c) > 47 and ord(c) < 58:
                    num_str += c
                else:
                    break
        
        if len(num_str) == 0 or len(num_str) == 1 and (num_str == '+' or num_str == '-'):
            return 0
        else:
            if num_str == '-':
                num = -1 * int(num_str[1:])
            elif num_str == '+':
                num = int(num_str[1:])
            else:
                num = int(num_str)

        if num >= 2**31:
            num = 2**31 - 1
        elif num <= -2**31:
            num = -2**31
        
        return num
    
if __name__ == "__main__":
    test = Solution()
    print(test.myAtoi("34"))