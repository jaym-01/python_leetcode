# note that arrays do not have a contant time complexity when appending elements
# to solve this issue, a doubly linked list can be used
# and only a pointer to the top of the stack kept
# and another doubly linked list mainting the order

class MinStack:

    def __init__(self):
        self.stack = []
        self.minPointers = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.minPointers) > 0 and self.stack[self.minPointers[-1]] > val) or len(self.minPointers) == 0:
            self.minPointers.append(len(self.stack) - 1)
        

    def pop(self) -> None:
        if self.minPointers[-1] == len(self.stack) - 1:
            del self.minPointers[-1]

        if len(self.stack) > 0:
            del self.stack[-1]

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minPointers) > 0:
            return self.stack[self.minPointers[-1]]
