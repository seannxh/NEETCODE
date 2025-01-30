
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp = []
        mini = self.stack[-1] 

        while len(self.stack):
            mini = min(mini, self.top()) #this gets the top which is -1 index of the stack and gets the minimum
            temp.append(self.stack.pop())# appends the end of the stack to temp and removes the element that was added from the stack       

        while len(temp):
            self.stack.append(temp.pop()) # this loop adds the thing back to it
        return mini #returns the mini at the last


def main():
    min_stack = MinStack()
    
    # Push elements
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print("Minimum:", min_stack.getMin())  # Should return -3
    
    # Pop top element
    min_stack.pop()
    print("Top:", min_stack.top())  # Should return 0
    print("Minimum:", min_stack.getMin())  # Should return -2

if __name__ == "__main__":
    main()




numlist = [1, 2, 3]

print(numlist.pop())
