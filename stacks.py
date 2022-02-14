# Stack : LIFO Datastructure (all the push and pop operations are from the top of the stack)

class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        # Pushing operation by appending an item to the top of the list
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:  # popping an item from the top of the stack if its length was greather than 0
            return self.stack.pop()

        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            # here we are doing the peek operation which takes the last item and print it without popping it out from the list
            return self.stack[len(self.stack) - 1]

    def __str__(self):
        return str(self.stack)


# Test code for the wrapper class
stack = Stack()
stack.push(4)
stack.push(6)
stack.push(1)
print(stack)
# Results : [4,6,1] 1 the last item is not popped because we've declared the popping operations just after we printed out the list
print(stack.pop())

# Now if we print out the stack we will see that it misses the last item and that's because we popped it out before

print(stack)  # Results : [4,6]
