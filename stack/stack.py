class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, element):
        """Takes in an element, attaches it to the end of the list 
        and returns nothing.
        Runtime for method is O(1), constant time
        """
        self.items.append(element)
        pass

    def pop(self):
        """
        Removes the last element from the list and returns it.
        O(1) time comlexity. Constant time
        """
        if(self.items):
            return self.items.pop()
        return None
    
    def peek(self):
        """
        Returns the last element from the list without removing it
        O(1) time complexity, constant time
        """
        if(self.items):
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the size of the list.
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a boolean whether the stack is empty. O(1) time complexity, testing for equality
        """
        return self.items == []

if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push("two")
    my_stack.pop()
    my_stack.push("three")
    print(my_stack.items)

        