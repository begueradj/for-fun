class EmptyStack(Exception):
    def __init__(self):
        super().__init__('Stack is empty: invalid operation!')

class Node:

    def __init__(self):
        self.data = None
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def push(self, item):
        self.node = Node()
        self.node.data = item
        self.node.next = self.head
        self.head = self.node
        self.size += 1

    def pop(self):
        if self.head == None:
            raise EmptyStack
        self.head_item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return self.head_item



if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print('size: {}'.format(stack.get_size()))
    print(stack.pop())
    print(stack.get_size())
