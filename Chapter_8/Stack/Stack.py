# Stack class

class Stack():
    "Stack class implements a last in first out LIFO algorithm"
    def __init__(self, starting_stack_list=None):
        if starting_stack_list is None:
            self.datalist = []
        else:
            self.datalist = starting_stack_list[:] #make a copy

    
    def push(self, item):
        self.datalist.append(item)

    def pop(self):
        if len(self.datalist) == 0:
            raise IndexError
        element = self.datalist.pop()
        return element

    
    def peek(self):
        # Retrieve the top item, without removing it
        item = self.datalist[-1]
        return item

    def getsize(self):
        nElements = len(self.datalist)
        return nElements

    def show(self):
        # Show the stack in a vertical orientation
        print("Stack is:")
        for value in reversed(self.datalist):
            print(' ', value)


print("__name__")